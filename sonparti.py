import json
import os

# JSON dosyasını oku
json_file_path = "structured-output/Birkamyon14.jpg.json"

with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Metin verilerini al
text_data = ""
for item in data:
    if "text" in item:
        text_data += item["text"] + "\n"

# Metnin ilk 3 kelimesini al
ilk_uc_kelime = text_data.split(" ")[:3]

# Dosya adı için ilk 3 kelimeyi kullan
output_txt_file_path = "_".join(ilk_uc_kelime) + ".txt"

# "tümCıktılar" klasörüne kaydet
output_txt_file_path = os.path.join("tümCıktılar", output_txt_file_path)

with open(output_txt_file_path, "w") as txt_file:
    txt_file.write(text_data)

print("Metin dosyası başarıyla oluşturuldu:", output_txt_file_path)




