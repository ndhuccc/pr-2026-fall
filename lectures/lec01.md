# Lecture 01:課程介紹與圖形識別概論

> 週次:第 1 週(2026-09-07)｜進度:Introduction / Course Overview & Introduction to Pattern Recognition

## 學習目標

- 說明圖形識別要解決的問題,並舉出文字、影像、聲音的例子
- 了解本課程的主題架構與評分方式(見 [`syllabus.md`](../syllabus.md)、[`schedule.md`](../schedule.md))
- 理解「特徵 → 分類器 → 類別」的基本流程

## 1. 什麼是圖形識別

圖形識別是讓電腦依據資料的特徵,把輸入歸入某一個類別。輸入可以是文字、影像或聲音。

處理流程(概念上):

- 原始資料(文字 / 影像 / 聲音)
- 特徵萃取(Feature Generation):把資料轉成可比較的數值向量
- 特徵選取(Feature Selection):保留有鑑別力的特徵
- 分類器(Classifier):依特徵決定類別
- 類別輸出

## 2. 課程主題

本課程的核心問題是:**如何設計特徵與分類器,使電腦能正確區分不同類別。** 主題依序為:

- 貝氏分類器:以機率與風險做決策
- 線性與非線性分類器:感知機、支持向量機、神經網路、核方法與決策樹
- 特徵選取與萃取:特徵選擇方法、PCA 與 LDA
- 樣板匹配:距離量測與動態時間規整(DTW)
- 上下文相關分類:Markov 模型與隱藏式 Markov 模型(HMM)
- 分群:K-means、階層式分群與評估

各週細節見 [`schedule.md`](../schedule.md)。

## 3. 符號約定

| 符號 | 意義 |
|---|---|
| $\mathbf{x} \in \mathbb{R}^d$ | 特徵向量(d 維) |
| $\omega_i$ | 第 $i$ 個類別 |
| $P(\omega_i)$ | 類別 $\omega_i$ 的先驗機率 |
| $p(\mathbf{x} \mid \omega_i)$ | 在類別 $\omega_i$ 下的條件機率密度 |
| $g_i(\mathbf{x})$ | 第 $i$ 類的判別函數 |

## 4. 最簡單的決策規則

給定判別函數 $g_1(\mathbf{x})$ 與 $g_2(\mathbf{x})$,決策規則為:

$$
\text{若 } g_1(\mathbf{x}) > g_2(\mathbf{x}),\ \text{則判為 } \omega_1;\ \text{否則判為 } \omega_2
$$

如何定義 $g_i(\mathbf{x})$,是第 2 週「貝氏決策理論」的主題。

## 5. 小結

- 圖形識別 = 由特徵決定輸入所屬的類別
- 特徵的品質與分類器的選擇共同決定辨識效果
- 下一週:貝氏決策理論

## 延伸閱讀

見 [`references/`](../references/README.md)。
