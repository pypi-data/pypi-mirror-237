from commons.to_debug import NoDataStartedStruct
from commons.exception.read_tag_struct_exception import ReadTagStructException
from pyhirtlib.tag_reader.tag_elemnts.tag_element_atomic import TagElementAtomic
from tag_reader.tag_elemnts.tag_element_reader import TagElementReader
from tag_reader.tag_elemnts.tag_element import ComplexTagElement, TagElement
from tag_reader.tag_elemnts.tag_element_dict import ChildTagElement, RootTagElement
from tag_reader.headers.tag_struct_table import TagStruct
from tag_reader.tag_elemnts.tag_element_type import BLOCKS, TagElemntType, TagStructType
from tag_reader.tag_layouts import TagLayouts
from tag_reader.tag_file import  TagFile
from events import Event

class TagFileMap:
    def __init__(self):
        self.blocks:{int, ComplexTagElement} = {}
        self.datas = {}
        self.refers = {}
        
class TagParse:
    def __init__(self, group:str):
        self.debug = False
        self.tagFile = TagFile()
        self.tagRootElemnt : RootTagElement= None
        self.reader : TagElementReader = None
        self.tagFile.evetToCall = self.doSomeOn
        self.tagFile.tag_struct_table.AddSubscribersForOnEntryRead(self.onEntryRead)
        self.group = group
        self.xml_template =None
        self.tag_structs_list : {int,TagFileMap} = {}

    def readIn(self, f, p_xml_tamplate = None):
        if p_xml_tamplate is None:
            self.xml_template = TagLayouts.Tags(self.group)
        #self.tag_structs_list[0]=self.xml_template[0]
        self.tagFile.readIn(f)
        
        #tagFile.readInOnlyHeader(f_t)

    def doSomeOn(self, params):
        pass

    def onEntryRead(self, f, entry: TagStruct):
        if not (entry is None):
            if entry.field_data_block_index == -1:
                pass
                #return
            
            tag: ComplexTagElement = None
            if entry.type_id_tg != TagStructType.Root:
                tag = self.tag_structs_list[entry.parent_entry_index].blocks[entry.field_offset]
                if (tag.L.T == TagElemntType.Struct):
                    if entry.type_id_tg != TagStructType.NoDataStartBlock:
                        raise ReadTagStructException(str(f), entry)
                
                if tag.L.E["hash"].upper() != entry.GUID.upper():
                    print("No equal hash")
            else:
                self.tagRootElemnt=self.reader.getTagElemnt(self.xml_template[0])
                tag = self.tagRootElemnt
                tag.readTagElemnt(f, 0, entry.field_data_block.offset_plus, entry, None)
                

            
            outresult = TagFileMap()
            
            if entry.info.n_childs != -1:
                if tag.L.T == TagElemntType.RootTagInstance:
                    self.readTagDefinition(f,entry,tag.L, tag, outresult,0)
                else:
                    for x in range(entry.info.n_childs): 
                        sub_child_elemnt = self.reader.struct_factory.getChildTagElemnt(tag.L)
                        sub_child_elemnt.index = x
                        sub_child_elemnt.parent = tag
                        sub_child_elemnt.readTagElemnt(f, 0, 0, entry, tag)
                        s = self.readTagDefinition(f, entry,tag.L, sub_child_elemnt, outresult,int(tag.L.E['size'])*x)
                        tag.array.append(sub_child_elemnt)
            else:
                pass
            self.tag_structs_list[entry.entry_index] = outresult
            if self.debug:
                if tag.L.T == TagElemntType.RootTagInstance:
                    assert(tag.L.E["hash"]==  entry.GUID.upper())
                    assert(entry.type_id_tg == TagStructType.Root)
                else:
                    assert tag.L.E["hash"]==entry.GUID.upper(), f"No equal hash {tag.L.E['hash']} == {entry.GUID.upper()}"
        pass
        
    def readTagDefinition(self,f, entry: TagStruct, tags: TagLayouts.C, parent: ComplexTagElement,outresult: TagFileMap, field_offset:int = 0) -> int:
        parent.onStartEnd(True)
        result = 0
        for address in tags.B:
            child_lay_tag = tags.B[address]
            child_tag_elemt = self.reader.getTagElemnt(child_lay_tag)
            child_tag_elemt.parent = parent
            result+= child_lay_tag.S
            parent.dict[child_lay_tag.N] = child_tag_elemt
            if child_tag_elemt is TagElementAtomic:
               child_tag_elemt.onStartEnd(True)
            child_tag_elemt.readTagElemnt(f, address, field_offset + entry.field_data_block.offset_plus, entry, parent)
            if child_tag_elemt is TagElementAtomic:
               child_tag_elemt.onStartEnd(False)
            self.verifyAndAddTagBlocks(outresult, child_tag_elemt, field_offset + address)
            if child_lay_tag.T == TagElemntType.Struct:
                self.readTagDefinition(f, entry, child_lay_tag, child_tag_elemt, outresult, field_offset + address)
            elif child_lay_tag.T == TagElemntType.Array:
                for _k in range(child_lay_tag.E["count"]):
                    sub_child_elemnt = self.reader.struct_factory.getChildTagElemnt(child_lay_tag)
                    sub_child_elemnt.index = _k
                    sub_child_elemnt.parent = child_tag_elemt
                    sub_child_elemnt.readTagElemnt(f, address, field_offset + entry.field_data_block.offset_plus, entry, child_tag_elemt)
                    self.readTagDefinition(f, entry, child_lay_tag, sub_child_elemnt, outresult, field_offset + address)
                    child_tag_elemt.array.append(sub_child_elemnt)

        parent.onStartEnd(False)
        return result

    def verifyAndAddTagBlocks(self, tag_maps: TagFileMap, child_item: TagElement, field_offset: int):
        if child_item.L.T == TagElemntType.Data:
            tag_maps.datas[field_offset] = child_item
            return
        elif child_item.L.T == TagElemntType.TagReference:
            tag_maps.refers[field_offset] = child_item
            return
        elif child_item.L.T == TagElemntType.Struct:
            if child_item.L.E["comp"] == "1" : 
                tag_maps.blocks[field_offset] =  child_item
            return
        elif child_item.L.T == TagElemntType.Block:
            tag_maps.blocks[field_offset] =  child_item
            return
        elif child_item.L.T == TagElemntType.ResourceHandle:
            tag_maps.blocks[field_offset] =  child_item
            return
        else:
            return