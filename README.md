# CS532_Project
# Vietnamese Driving License Information Extractor

Chương trình sẽ detect các vị trí có thông tin quan trọng với Yolov5, sau đó dùng VietOCR để đọc text có trong các vị trí đã detect được.

## Danh sách thành viên
- Hoàng Ngọc Bá Thi
- Phan Minh Nhật
- Trần Hồ Thiên Phước
- Lê Võ Tiến Phát

## Cách cài đặt và chạy chương trình
### Tạo và kích hoạt môi trường ảo với anaconda
```
conda create --name yourenv
```

```
conda activate yourenv
```
### Clone repository
```
git clone https://github.com/KBGIBN/CS532_project
```

### Cài đặt các thư viện cần thiết trong requirements.txt
```
conda install -c anaconda pip
```
```
pip install -r requirements.txt
```
### Tải weight của Yolov5 và VietOCR
Tải weight tại: https://drive.google.com/drive/u/1/folders/1ZYBLMrWoleMNC3yyAFLfPO9PXCA3HdMB

File weight của VietOCR là transformerocr.pth phải được lưu trong folder CS532_project.  

### Chạy chương trình 
Có thể sử dụng
```
flask run
```
hoặc
```
python app.py
```
Khi server đã được khởi chạy, truy cập vào địa chỉ: http://127.0.0.1:5000

Ta sẽ được giao diện như sau: 
![demo](demo.jpg)
