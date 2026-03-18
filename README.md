# AI Machine Data Analyzer

## 📌 專案概述
這個專案模擬工業機台資料監控系統，使用 Python 讀取 PLC 模擬資料，並自動偵測異常數據。  
透過可互動的 **Streamlit Dashboard**，使用者可以即時查看原始資料、異常點和機台數據曲線。

---

## ⚙️ 功能 Features
- 讀取 CSV 模擬 PLC 資料 (`time, temperature, pressure, cycle_time`)  
- 異常偵測：使用 **Isolation Forest** AI 模型自動找出異常點  
- 可視化：繪製溫度與壓力曲線  
- Streamlit Dashboard：瀏覽器即時查看資料與異常

---

## 🖼 Dashboard 截圖 Demo

![Demo](demo.png)

---

## 🛠 技術棧 Tech Stack
- Python 3.x  
- pandas
- matplotlib
- scikit-learn
- Streamlit  

---

## 🚀 快速上手 How to Run
1. 安裝套件：
```bash
pip install -r requirements.txt

==================================

2.執行 Dashboard：

streamlit run dashboard.py

==================================

Dashboard 功能：

左側瀏覽資料表格

偵測異常並列出表格

顯示溫度與壓力曲線

CLI 分析：

python main.py

在 console 印出資料與異常點

==================================

📊 範例資料 Example Data

CSV 欄位：

time,temperature,pressure,cycle_time
1,75,30,5
2,76,31,5.2
3,75,29,4.9
4,77,32,5.1
5,75,30,5
6,78,33,5.3
7,76,31,5.1
8,75,29,5
9,77,32,5.2
10,76,30,5
11,90,50,8   # 異常值範例
12,74,28,4.8

==================================

🔧 專案結構 Project Structure
ai-machine-data-analyzer/
│
├── data/                 # 模擬資料 CSV
│   └── sample_data.csv
├── src/                  # Python 模組
│   ├── load_data.py
│   ├── analyze.py
│   └── anomaly.py
├── dashboard.py          # Streamlit Dashboard
├── main.py               # CLI 版本分析程式
├── requirements.txt
├── demo.png              # Dashboard 範例截圖
└── README.md

==================================

💡 使用說明 Tips

CSV 必須包含完整欄位：time, temperature, pressure, cycle_time

Isolation Forest 的 contamination 參數可調整異常偵測靈敏度

異常資料會被標記為 -1，正常資料為 1

Streamlit Dashboard 需在專案根目錄執行，以正確讀取 src 模組與 CSV

==================================

🔮 未來改進 Future Improvements

連接真實 PLC 或 OPC UA 資料

Dashboard 增加互動圖表、篩選功能或多機台視圖

引入時間序列模型 (LSTM / Autoencoder) 進行異常偵測

支援多使用者即時監控工廠機台

==================================

📌 專案價值 Value

面試展示：完整 AI + 自動化分析流程

產品感：即時 Dashboard，異常偵測可視化

可拓展性：可直接接入工業自動化系統