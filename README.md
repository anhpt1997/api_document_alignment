# api_document_alignment

Hướng dẫn cài đặt Word2Vec
+ Download model w2vec từ link sau: https://drive.google.com/file/d/0B1GKSX6YCHXlMTVZNkFEYzRyd1E/view
+ Để đường dẫn model tại thư mục chứa folder api

Hướng dẫn cài đặt Vncore nlp
+ cài đặt môi trường java trên ubuntu ---> để cài đặt vncore nlp 
+ clone vncore nlp bằng câu lệnh sau: git clone https://github.com/vncorenlp/VnCoreNLP.git
+ install vncore nlp bằng command line: pip install vncorenlp
+ sau khi clone và install vncorenlp, muốn sử dụng nó ta phải di chuyển vào folder vncore nlp bằng command: cd VNcore nlp
+ run command sau: vncorenlp -Xmx2g FULL-PATH-to-VnCoreNLP-jar-file -p 9000 -a "wseg" trong đó : FULL-PATH-to-VnCoreNLP-jar-file là tên file .jar trong folder vừa clone về , giữ nguyên tiến trình đang chạy, không dc tắt nó trên terminal.


Chạy api tại file api.py
+Ví dụ: python api.py test_raw_vn.txt test_raw_khrme.txt km
+trong đó:  - test_raw_vn.txt là file chứa doc thuộc ngôn ngữ việt nam 
            - test_raw_khrme.txt là file chứa ngôn ngữ hiếm <không nhất thiết phải là khrme>
            - km chỉ kí hiệu của ngôn ngữ khơ me: Đối với tiếng trung là zh-cn, đối với tiếng lào là: lo