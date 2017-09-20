#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from trietree import TrieTree
from model_handler import ModelHandler
from syllable_handler import SyllableHandler
from lexi_handler import LexiHandler

class Input(object):
    def __init__(self, model_file, syllable_file, syl2chinese):
        self.modelhandler = ModelHandler(model_file)
        self.syllablehandler = SyllableHandler(syllable_file)
        self.lexihandler = LexiHandler(syl2chinese)
        self.Init()

    def Init(self):
        self.syllablehandler.Init()
        self.lexihandler.Init()
        self.modelhandler.Init()

    def SpellSplit(self, pinyin):
        return self.syllablehandler.SpellSplit(pinyin)

    def SpellToChi(self, spells):
        """
        改进字典树 拼音转汉字
        """
        ch = self.lexihandler.GetChineseFromSpells(spells)
        if ch:
            return ch
        else:
            #没找到 需要在单个字符查找
            for i in spells:
                res = self.lexihandler.GetChineseFromSpells([i,])
                if res:
                    for k in res:
                        print k
                else:
                    print "not found ", i


    def GetChineseFromPinyin(self, pinyin):
        spelllist = self.SpellSplit(pinyin)
        return self.SpellToChi(spelllist)


if __name__ == '__main__':
    input = Input("text.train", "syllable.bdt", "lexicon.bdt")
    print input.GetChineseFromPinyin('zhendebuhaowan')
    import sys
    sys.exit(0)
    spells = ['hangmu','hangkongmujianzhandouqun','hangkonghangtiangongyebu','zhendebuhaowan']
    for s in spells:
        res = input.GetChineseFromPinyin(s)
        for item in res:
            print item
