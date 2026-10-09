# 圖型識別(AIIA50260)— 2026 秋季

> 國立東華大學 資訊工程學系｜授課教師:江政欽 教授｜聯絡信箱:ccchiang@gms.ndhu.edu.tw

課程網站:<https://ndhuccc.github.io/pr-2026-fall/>

> 🤖 **老師使用 AI Agent 經營本課程?** 請先看 `START_HERE.md`,並把 `AGENTS.md` 交給您的 AI。

## 課程簡介

本課程介紹圖形識別（Pattern Recognition）之基礎理論與應用技術，涵蓋貝氏分類器（Bayes Classifiers）、線性與非線性分類器（Linear and Nonlinear Classifiers）、特徵選取與萃取（Feature Selection and Generation）、樣板匹配（Template Matching）、上下文相關分類（Context-Dependent Classification）以及分群方法（Clustering）等主題。透過理論講授與實作練習，使學生具備運用電腦對文字、影像、聲音等各類資料進行分類與辨識之能力。

## 學習目標

完成本課程後,你將能夠:

1. 說明課程核心概念與數學基礎(例如:$\mathbf{y} = W\mathbf{x} + \mathbf{b}$)
2. 以 Python / PyTorch 實作並驗證模型
3. 閱讀與討論相關文獻
4. 完成一項期末專題

## 先備知識

- 微積分、線性代數、機率與統計
- Python 基礎

## Repo 導覽

| 目錄 / 檔案 | 內容 |
|---|---|
| [`syllabus.md`](syllabus.md) | 課程大綱、評分、規範 |
| [`schedule.md`](schedule.md) | 週次進度與截止日 |
| [`lectures/`](lectures/) | 每週講義(Markdown + LaTeX) |
| [`slides/`](slides/) | 投影片(HTML / PDF) |
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
| 一對一討論 | Office Hour:{{OFFICE_HOUR}} |

## 授權

講義內容採 CC BY-NC-SA 4.0;程式碼採 MIT。詳見 [`LICENSE`](LICENSE)。
