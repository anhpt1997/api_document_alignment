from client import Translator
import time
import os
import unicodedata

translator = Translator()

def translate_file(file_in , file_out , src_lg = 'km' , dest_lg = 'vi'):
    with open('file_out','a+', encoding='utf-8') as f:
        f.seek(0)
        n_processed = len(f.readlines())
        print(n_processed,"sens have been processed")
        f.seek(0, os.SEEK_END)
        for i,line in enumerate(open(file_in, encoding='utf-8')):
            if i < n_processed:
                continue
            line = line.strip()
            ### Remove emoji icon that's not accepted by ChromeDriver
            line = ''.join(c for c in unicodedata.normalize('NFC', line) if c <= '\uFFFF')
            f.write(line+'\n'+translator.translate(line , src = src_lg , dest=dest_lg)+'\n')

doc = """
'វៀតណាមស្នើឱ្យក្រុមប្រទេស G20 ផ្តល់ការគាំទ្រផ្នែកហិរញ្ញវត្ថុនិងបច្ចេកវិទ្យាដល់ប្រទេសកំពុងអភិវឌ្ឍន៍ ក្នុងក្របខ័ណ្ឌនៃកិច្ចប្រជុំកំពូល G20 ដែលប្រារព្ធឡើងតាមប្រព័ន្ធវីដេអូ នាយប់ថ្ងៃទី ២២ ខែវិច្ឆិកា (វេលាម៉ោងនៅវៀតណាម) លោកនាយករដ្ឋមន្រ្តីវៀតណាម Nguyen Xuan Phuc បានចូលរួមសម័យប្រជុំពិភាក្សាលើកទី ២ ជាមួយប្រធានបទ “កសាងអនាគតប្រកបដោយចីរភាព បរិយាប័ន្ននិងមានភាពធន់”។ ថ្លែងនៅក្នុងកិច្ចប្រជុំ លោកនាយករដ្ឋមន្រ្តី Nguyen Xuan Phuc បានសង្កត់ធ្ងន់ថាសន្តិភាព ស្ថិរភាព កិច្ចសហប្រតិបត្តិការនិងការអភិវឌ្ឍន៍គឺជាល័ក្ខខណ្ឌចម្បង សម្រាប់ការអភិវឌ្ឍប្រកបដោយចីរភាពនិងបរិយាបន្ន។ ការណ៍នេះ អាចធ្វើទៅបានលុះត្រាដែលទំនាក់ទំនងអន្តរជាតិត្រូវបានរក្សា តាមរយៈប្រព័ន្ធពហុភាគី ផ្អែកលើច្បាប់ ហើយប្រទេសទាំងអស់ត្រូវគោរពគ្នា\u200b មានការយោគយល់គ្នា មានកិច្ចសហប្រតិបត្តិការនិងការជឿទុកចិត្តគ្នាទៅវិញទៅមក។ នេះនឹងជាបុព្វបទដ៏សំខាន់មួយសម្រាប់ G20, អង្គការសហប្រជាជាតិនិងស្ថាប័នពហុភាគី ពង្រីកនូវតួនាទីរបស់ខ្លួន ក្នុងការដោះស្រាយបញ្ហាពិភពលោកក្នុងបរិបទថ្មី។ នាយករដ្ឋមន្រ្តីលោក Nguyen Xuan Phuc បានថ្លែងថា៖ “ដើម្បីអនុវត្តប្រកបដោយជោគជ័យនូវគោលដៅអភិវឌ្ឍន៍ប្រកបដោយចីរភាពរបស់អង្គការសហប្រជាជាតិ (SDG) 
"""

for i in range(1000000):
    print(i)
    dest = translator.translate(text = doc, dest="vi", src="km")
    time.sleep(2)
    print('des', dest)
# translate_file(file_in ='test_raw_khrme.txt' , file_out = 'test_translate_vn.txt')
