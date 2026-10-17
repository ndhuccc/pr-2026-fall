# 課程大綱(Syllabus)

## 基本資訊

| 項目 | 內容 |
|---|---|
| 課程名稱 | 圖型識別(Pattern Recognition) |
| 課號 | AIIA50260 |
| 學期 | 2026 秋季 |
| 修別 | 碩士 / 選修 |
| 學分 / 時數 | 3 學分 / 3 小時 |
| 上課時間地點 | 週一 14:10–17:00 |
| 授課教師 | 江政欽 教授(ccchiang@gms.ndhu.edu.tw) |
| 助教 | |
| Office Hour | |

## 課程描述

本課程介紹圖形識別(Pattern Recognition)之基礎理論與應用技術,涵蓋貝氏分類器(Bayes Classifiers)、線性與非線性分類器(Linear and Nonlinear Classifiers)、特徵選取與萃取(Feature Selection and Generation)、樣板匹配(Template Matching)、上下文相關分類(Context-Dependent Classification)以及分群方法(Clustering)等主題。透過理論講授與實作練習,使學生具備運用電腦對文字、影像、聲音等各類資料進行分類與辨識之能力。

## 課程目標

學生完成本課程後,能建立圖形識別的理論與實作基礎,運用電腦對文字、影像、聲音等各類資料進行分類與辨識。具體學習目標如下(同首頁「學習目標」):

1. 貝氏分類器:說明貝氏決策理論、判別函數與錯誤界限,並能進行機率密度估計
2. 線性與非線性分類器:理解並實作感知器、線性判別函數、支持向量機、類神經網路、核方法與決策樹
3. 特徵選取與萃取:運用特徵選取方法、PCA 與 LDA 降低資料維度
4. 樣板匹配:運用距離度量與動態時間校正(DTW)比對序列與樣式
5. 上下文相關分類:說明馬可夫模型與隱馬可夫模型(HMM)並應用於序列資料
6. 分群方法:運用 K-means 與階層式分群並評估結果
7. 實作與專題:以 Python 實作並驗證方法,完成期末專題與發表

## 教科書與參考資料

- 主要教材:Sergios Theodoridis & Konstantinos Koutroumbas, Pattern Recognition, 4th Edition, Academic Press/Elsevier, 2008. ISBN 978-1-59749-272-0
- 其他參考:見 [`references/`](references/)

## 授課進度

各週主題與日期見 [`schedule.md`](schedule.md),本學期共 17 週。

## 評分方式

| 項目 | 比例 |
|---|---|
| 平時成績(含出缺席) | 20% |
| 期中考 | 25% |
| 期末考 | 35% |
| 作業 | 20% |

總成績計算:

$$
S = 0.20\,S_{\text{part}} + 0.25\,S_{\text{mid}} + 0.35\,S_{\text{final}} + 0.20\,S_{\text{hw}}
$$

> 比例依教學計畫表。任何異動記錄於 [`CHANGELOG.md`](CHANGELOG.md)。

## 作業繳交規範

作業採「學生自建個人作業 Repo、邀請教師為協作者、打標籤 `hwNN-submit` 繳交」的流程,並搭配課堂**作業理解測驗**(題目取自學生自己的程式)校準作業分數。完整規範見 [作業說明](assignments/README.md)。遲交處理與扣分規則尚待教師訂定。

## 學術誠信

- 允許討論想法,但**程式碼與報告須獨立完成**
- 引用他人程式碼、模型或生成式 AI 輔助,須於作業中**明確標註來源與用途**
- 抄襲或代寫依校規處理

## 生成式 AI 使用政策

- 所有作業與期末專題**可以使用任何 AI 工具**。
- 唯一不可退讓的是:**你自己的思考必須在 Repo 裡看得見**。
- 每次有 AI 協助的 commit,訊息要依下列格式寫(以下為示範):

  ```
  fix: 修正輸出層反向傳播的符號錯誤
  AI-Tool: ChatGPT (GPT-4o)
  AI-Prompt: "我的梯度和數值梯度不一致,請檢查輸出層的反向傳播"
  AI-Reason: 數值梯度檢查沒通過,想找出錯誤位置
  Human-Judgment: 我自己重新推導了 dL/dz,確認 AI 指出的符號錯誤成立後才修改
  ```

- 請**多次小量提交**,不要在截止前一次大量 commit。
- AI agent 可以代為撰寫並推送 commit,但**必須先把完整訊息給你確認**。
- 教師可能隨機請你口頭說明任何一個 commit。
- 每份 `report.md` 末尾仍須有「AI 使用聲明與引用」(見 [作業說明](assignments/README.md))。

## 課堂規範

- 尊重他人,討論區禁止人身攻擊
- 請勿在公開 Issue / Discussion 張貼個資、學號、成績
