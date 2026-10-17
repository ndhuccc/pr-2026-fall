# 圖型識別(AIIA50260)— 2026 秋季

> 國立東華大學 資訊工程學系｜授課教師:江政欽 教授｜聯絡信箱:ccchiang@gms.ndhu.edu.tw

課程網站:<https://ndhuccc.github.io/pr-2026-fall/>

> 🤖 **老師使用 AI Agent 經營本課程?** 請先看 `START_HERE.md`,並把 `AGENTS.md` 交給您的 AI。

## 課程簡介

本課程介紹圖形識別（Pattern Recognition）之基礎理論與應用技術，涵蓋貝氏分類器（Bayes Classifiers）、線性與非線性分類器（Linear and Nonlinear Classifiers）、特徵選取與萃取（Feature Selection and Generation）、樣板匹配（Template Matching）、上下文相關分類（Context-Dependent Classification）以及分群方法（Clustering）等主題。透過理論講授與實作練習，使學生具備運用電腦對文字、影像、聲音等各類資料進行分類與辨識之能力。

## 學習目標

本課程的總目標:建立圖形識別(Pattern Recognition)的理論與實作基礎,能運用電腦對文字、影像、聲音等各類資料進行分類與辨識。完成本課程後,你將能夠(括號為對應的評量方式):

1. **貝氏分類器(Bayes Classifiers)**:能**推導**最小錯誤率貝氏決策規則與判別函數並**計算**錯誤界限;能以最大概似、貝氏推論、EM 與無母數方法**估計**機率密度,並**實作**貝氏與單純貝氏分類器,在資料集上**比較**其正確率(HW01、期中考)
2. **線性與非線性分類器(Linear and Nonlinear Classifiers)**:能**推導**並**實作**感知器、最小平方與 SVM 的訓練演算法;能**說明**類神經網路、核方法與決策樹的原理,並依資料特性**選擇**合適的分類器且**說明理由**(期中考、期末專題)
3. **特徵選取與萃取(Feature Selection and Generation)**:能**計算** PCA 與 LDA 的投影方向,並運用特徵選取方法**降低維度**;能以實驗**驗證**降維對辨識正確率的影響(期末考、期末專題)
4. **樣板匹配(Template Matching)**:能**計算**常用距離度量,並**實作**動態時間校正(DTW)以**比對**長度不同的序列(期末考)
5. **上下文相關分類(Context-Dependent Classification)**:能**寫出**馬可夫模型與隱馬可夫模型(HMM)的參數,並**執行**前向演算法與 Viterbi 解碼,用於序列資料的辨識(期末考)
6. **分群方法(Clustering)**:能**實作** K-means 與階層式分群,並以**評估指標**判斷分群結果的優劣(期末考、期末專題)
7. **實作與專題**:能以 Python **實作並驗證**上述方法於文字、影像或聲音資料,**撰寫**實驗報告並於期末**發表**,且**標註**資料來源與 AI 工具使用(期末專題與發表)

## 先備知識

- 微積分、線性代數、機率與統計
- Python 基礎

## Repo 導覽

| 目錄 / 檔案 | 內容 |
|---|---|
| [`syllabus.md`](syllabus.md) | 課程大綱、評分、規範 |
| [`schedule.md`](schedule.md) | 週次進度與截止日 |
| [`lectures/`](lectures/) | 每週講義(Markdown + LaTeX)。同一週可有多份:`lecNN.md` 是正課,`lecNN-<代號>.md` 是補充或自主學習教材(見 `schedule.md`) |
| [`slides/`](slides/) | 投影片(JianBauDau JSON、PPTX、PDF 或 HTML) |
| [`notebooks/`](notebooks/) | 實作 Notebook(可於 Colab 開啟) |
| [`labs/`](labs/) | 實驗(尚未加入,之後依課程進度新增) |
| [`assignments/`](assignments/) | 作業說明與評分標準 |
| [`projects/`](projects/) | 期末專題說明與里程碑 |
| [`exams/`](exams/)、[`quizzes/`](quizzes/) | 考試範圍、考古題、測驗 |
| [`references/`](references/) | 參考文獻與連結 |
| [`study-guide/`](study-guide/) | 自學指引與複習地圖 |
| [`FAQ.md`](FAQ.md)、[`glossary.md`](glossary.md) | 常見問題、術語表 |
| [`CHANGELOG.md`](CHANGELOG.md) | 學期中異動紀錄 |

## 快速開始

```bash
# 1. 取得專案
git clone https://github.com/ndhuccc/pr-2026-fall
cd pr-2026-fall

# 2. 建立環境
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. 驗證環境(實驗加入後,此處會列出測試指令)
```

或直接使用 **GitHub Codespaces**(點選 *Code → Codespaces → Create*),環境已自動設定。

## 如何取得協助

| 需求 | 管道 |
|---|---|
| 課程內容提問 | [Issues → 提問](https://github.com/ndhuccc/pr-2026-fall/issues/new/choose) 或 Discussions |
| 講義/作業勘誤 | [Issues → 勘誤回報](https://github.com/ndhuccc/pr-2026-fall/issues/new/choose) |
| 請假/補交/成績申請 | [Issues → 申請](https://github.com/ndhuccc/pr-2026-fall/issues/new/choose)(**請勿**在公開 Issue 填寫個資) |
| 一對一討論 | Office Hour: |

## 授權

講義內容採 CC BY-NC-SA 4.0;程式碼採 MIT。詳見 [`LICENSE`](LICENSE)。
