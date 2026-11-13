# 週次進度表(Schedule)

學期:2026 秋季｜第 1 週起始日:2026-09-07｜本學期共 17 週
依教學計畫表(115 學年第 1 學期)編寫。因兩個週一放假,期中前的 Bayes 與 Linear 兩組單元各合併為一次課;第 11 週的樣板匹配(原第 11、12 週)合併為一次課,其後單元各提前一週。

<span class="self-study">紫色字</span> = 自主學習的知識點(其餘為課堂講授)。

| 週次 | 日期 | 主題 | 講義 | 備註 |
|:---:|---|---|---|---|
| 1 | 09/07 | Introduction / Course Overview & Introduction to Pattern Recognition | [KP01 導論：什麼是樣式識別](lectures/lec01.md) · [簡報](slides/lec01.jbd.json) | |
| 2 | 09/14 | Bayes Classifiers (1)+(2) – Bayesian Decision Theory; Discriminant Functions & Error Bounds(貝氏決策理論、判別函數與線性分類器) | [KP01 貝氏決策理論與判別函數](lectures/lec02.md) · [簡報](slides/lec02.jbd.json)；[KP02 線性分類器](lectures/lec02-linear-classifiers.md) · [簡報](slides/lec02-linear-classifiers.jbd.json) | 合併原計畫第 2、3 週;共 9 個知識點分三段(KP01–KP02) |
| 2 | 09/14 | Bayes Classifiers – Probability Density Estimation(機率密度估計:參數估計、貝氏推論與最大熵、混合模型與 EM、無母數密度估計) | [KP03 參數估計](lectures/lec02-parameter-estimation.md) · [簡報](slides/lec02-parameter-estimation.jbd.json)；[KP04 貝氏推論與最大熵](lectures/lec02-bayesian-inference.md) · [簡報](slides/lec02-bayesian-inference.jbd.json)；[KP05 混合模型與 EM](lectures/lec02-mixture-models-em.md) · [簡報](slides/lec02-mixture-models-em.jbd.json)；[KP06 無母數密度估計](lectures/lec02-nonparametric-density.md) · [簡報](slides/lec02-nonparametric-density.jbd.json) | KP03–KP06 |
| 2 | 09/14 | Bayes Classifiers – Naive Bayes, Nearest Neighbor & Bayesian Networks(單純貝氏、最近鄰居、貝氏網路與其推論) | [KP07 單純貝氏與最近鄰居](lectures/lec02-naive-bayes-and-nn.md) · [簡報](slides/lec02-naive-bayes-and-nn.jbd.json)；[KP08 貝氏網路](lectures/lec02-bayesian-networks.md) · [簡報](slides/lec02-bayesian-networks.jbd.json)；[KP09 貝氏網路推論](lectures/lec02-bayesian-network-inference.md) · [簡報](slides/lec02-bayesian-network-inference.jbd.json) | KP07–KP09 |
| 3 | 09/21 | Linear Classifiers (1) – Perceptron(感知器:分數、法向量、批次/線上演算法、收斂證明、口袋演算法) | [KP01 分數、法向量與距離](lectures/lec03-kp01-pilot.md) · [簡報](slides/lec03-kp01-pilot.jbd.json)；[KP02 批次感知器](lectures/lec03-kp02-batch-perceptron.md) · [簡報](slides/lec03-kp02-batch-perceptron.jbd.json)；[KP03 收斂證明](lectures/lec03-kp03-convergence.md){ .self-study } · [簡報](slides/lec03-kp03-convergence.jbd.json){ .self-study }；[KP04 線上感知器](lectures/lec03-kp04-online-perceptron.md) · [簡報](slides/lec03-kp04-online-perceptron.jbd.json)；[KP05 神經元與口袋](lectures/lec03-kp05-neuron-pocket.md) · [簡報](slides/lec03-kp05-neuron-pocket.jbd.json) | 合併原計畫第 4、5 週;共 16 個知識點分三段(KP01–KP05);KP03 為自主學習;KP01–KP03 簡報含逐步配音與核心推導頁(KP01 垂足與最近點、KP02 代價函數與次梯度、KP03 證明用三個量與逐筆錯誤界) |
| 3 | 09/21 | Linear Classifiers (1) – Linear Discriminant Functions(線性判別函數:Kesler 構造、最小平方、LMS、條件平均與偏差變異、邏輯迴歸) | [KP06 Kesler 構造](lectures/lec03-kp06-kesler.md) · [簡報](slides/lec03-kp06-kesler.jbd.json)；[KP07 最小平方與正交投影](lectures/lec03-kp07-mse-projection.md) · [簡報](slides/lec03-kp07-mse-projection.jbd.json)；[KP08 LMS 演算法](lectures/lec03-kp08-lms.md) · [簡報](slides/lec03-kp08-lms.jbd.json)；[KP09 最小平方解](lectures/lec03-kp09-least-squares.md) · [簡報](slides/lec03-kp09-least-squares.jbd.json)；[KP10 條件平均與最佳預測](lectures/lec03-kp10-conditional-mean.md){ .self-study } · [簡報](slides/lec03-kp10-conditional-mean.jbd.json){ .self-study }；[KP11 條件平均與事後機率](lectures/lec03-kp11-mse-posterior.md){ .self-study } · [簡報](slides/lec03-kp11-mse-posterior.jbd.json){ .self-study }；[KP12 偏差與變異](lectures/lec03-kp12-bias-variance.md){ .self-study } · [簡報](slides/lec03-kp12-bias-variance.jbd.json){ .self-study } · [基礎版簡報](slides/lec03-kp12-bias-variance-basic.jbd.json){ .self-study }；[KP13 邏輯迴歸](lectures/lec03-kp13-logistic.md) · [簡報](slides/lec03-kp13-logistic.jbd.json) | KP06–KP13;KP10、KP11、KP12 為自主學習;KP07、KP08、KP09、KP11、KP12、KP13 簡報含逐步配音與核心推導頁(KP07 多輸出拆解、KP08 向量步長上限、KP09 正規方程推導、KP11 平方損失拆解、KP12 偏誤與變異數算法、KP13 高斯對數比值);KP12 另有基礎版簡報(證據先行、每頁先想再揭曉,含配音) |
| 3 | 09/21 | Linear Classifiers (2) – Support Vector Machines(支持向量機:硬間隔、軟間隔、多類別 ECOC) | [KP14 硬間隔 SVM](lectures/lec03-kp14-hard-margin.md) · [簡報](slides/lec03-kp14-hard-margin.jbd.json) · [基礎版簡報](slides/lec03-kp14-hard-margin-basic.jbd.json)；[KP15 軟間隔與鬆弛變數](lectures/lec03-kp15-soft-margin.md) · [簡報](slides/lec03-kp15-soft-margin.jbd.json)；[KP16 多類別 ECOC](lectures/lec03-kp16-multiclass-ecoc.md) · [簡報](slides/lec03-kp16-multiclass-ecoc.jbd.json) | KP14–KP16;簡報含逐步配音與核心推導頁(KP14 拉格朗日與對偶、KP15 軟間隔拉格朗日與乘子上界、KP16 糾錯半徑的三角不等式證明);KP14 另有基礎版簡報(證據先行、每頁先想再揭曉,含配音) |
| 4 | 09/28 | 放假(孔子誕辰／教師節) | | 無上課 |
| 5 | 10/05 | Nonlinear Classifiers (1) – Neural Networks: Multilayer Perceptrons(多層感知器:XOR、兩層與三層感知器、多面體編碼、構造式方法) | [KP00 本章路線圖](lectures/lec05-kp00-overview.md) · [簡報](slides/lec05-kp00-overview.jbd.json)；[KP01 XOR 與一條線的極限](lectures/lec05-kp01-xor.md) · [簡報](slides/lec05-kp01-xor.jbd.json)；[KP02 兩層感知器](lectures/lec05-kp02-two-layer-perceptron.md) · [簡報](slides/lec05-kp02-two-layer-perceptron.jbd.json)；[KP03 多條線的編碼](lectures/lec05-kp03-polyhedral-codes.md) · [簡報](slides/lec05-kp03-polyhedral-codes.jbd.json)；[KP04 三層感知器](lectures/lec05-kp04-three-layer-perceptron.md) · [簡報](slides/lec05-kp04-three-layer-perceptron.jbd.json)；[KP05 構造式方法](lectures/lec05-kp05-constructive-methods.md) · [簡報](slides/lec05-kp05-constructive-methods.jbd.json) | KP00–KP05;KP00 是本章路線圖總覽 |
| 5 | 10/05 | Nonlinear Classifiers (1) – Neural Networks: Backpropagation(反向傳播:梯度、演算法、加速變形、代價函數) | [KP06 反向傳播的梯度](lectures/lec05-kp06-backprop-gradient.md) · [簡報](slides/lec05-kp06-backprop-gradient.jbd.json)；[KP07 反向傳播的演算法](lectures/lec05-kp07-backprop-algorithm.md) · [簡報](slides/lec05-kp07-backprop-algorithm.jbd.json)；[KP08 反向傳播的加速](lectures/lec05-kp08-backprop-speedups.md){ .self-study } · [簡報](slides/lec05-kp08-backprop-speedups.jbd.json){ .self-study }；[KP09 代價函數的選擇](lectures/lec05-kp09-cost-functions.md) · [簡報](slides/lec05-kp09-cost-functions.jbd.json) | KP06–KP09;KP08 為自主學習 |
| 5 | 10/05 | Nonlinear Classifiers (1) – Neural Networks: Network Size & Generalization(網路大小、泛化與早停、剪枝與正則化、權重共享) | [KP10 網路大小與早停](lectures/lec05-kp10-network-size.md){ .self-study } · [簡報](slides/lec05-kp10-network-size.jbd.json){ .self-study }；[KP11 剪枝與正則化](lectures/lec05-kp11-pruning-regularization.md){ .self-study } · [簡報](slides/lec05-kp11-pruning-regularization.jbd.json){ .self-study }；[KP12 權重共享](lectures/lec05-kp12-weight-sharing.md){ .self-study } · [簡報](slides/lec05-kp12-weight-sharing.jbd.json){ .self-study } | KP10–KP12;全部為自主學習 |
| 6 | 10/12 | Nonlinear Classifiers (2) – Generalized Linear Classifiers(廣義線性分類器:Cover 定理、多項式、RBF 網路、通用近似、PNN) | [KP13 廣義線性分類器](lectures/lec05-kp13-generalized-linear.md) · [簡報](slides/lec05-kp13-generalized-linear.jbd.json)；[KP14 Cover 定理](lectures/lec05-kp14-cover-theorem.md){ .self-study } · [簡報](slides/lec05-kp14-cover-theorem.jbd.json){ .self-study }；[KP15 多項式分類器](lectures/lec05-kp15-polynomial.md) · [簡報](slides/lec05-kp15-polynomial.jbd.json)；[KP16 RBF 網路](lectures/lec05-kp16-rbf.md) · [簡報](slides/lec05-kp16-rbf.jbd.json)；[KP17 通用近似定理](lectures/lec05-kp17-universal-approx.md){ .self-study } · [簡報](slides/lec05-kp17-universal-approx.jbd.json){ .self-study }；[KP18 機率神經網路](lectures/lec05-kp18-pnn.md) · [簡報](slides/lec05-kp18-pnn.jbd.json) | KP13–KP18;KP14、KP17 為自主學習;HW01 發佈 |
| 6 | 10/12 | Nonlinear Classifiers (2) – Kernel Methods(核方法:非線性 SVM 與 Mercer 核技巧、kernel perceptron、Representer 定理、穩健迴歸與 ridge) | [KP19 非線性 SVM 與核技巧](lectures/lec05-kp19-kernel-svm.md) · [簡報](slides/lec05-kp19-kernel-svm.jbd.json)；[KP20 核技巧的通用化](lectures/lec05-kp20-beyond-svm.md) · [簡報](slides/lec05-kp20-beyond-svm.jbd.json)；[KP21 表示定理與稀疏化](lectures/lec05-kp21-representer.md){ .self-study } · [簡報](slides/lec05-kp21-representer.jbd.json){ .self-study }；[KP22 穩健迴歸與脊迴歸](lectures/lec05-kp22-robust-ridge.md){ .self-study } · [簡報](slides/lec05-kp22-robust-ridge.jbd.json){ .self-study } | KP19–KP22;KP21、KP22 為自主學習 |
| 6 | 10/12 | Nonlinear Classifiers (2) – Decision Trees & Ensembles(決策樹、結合分類器、Boosting 與 AdaBoost、類別不平衡) | [KP23 決策樹](lectures/lec05-kp23-decision-tree.md) · [簡報](slides/lec05-kp23-decision-tree.jbd.json)；[KP24 結合分類器](lectures/lec05-kp24-combining.md) · [簡報](slides/lec05-kp24-combining.jbd.json)；[KP25 Boosting 與 AdaBoost](lectures/lec05-kp25-adaboost.md) · [簡報](slides/lec05-kp25-adaboost.jbd.json)；[KP26 類別不平衡](lectures/lec05-kp26-imbalance.md) · [簡報](slides/lec05-kp26-imbalance.jbd.json) | KP23–KP26 |
| 7 | 10/19 | Feature Selection and Generation (1) – Feature Selection Methods(特徵選擇:檢定、ROC/AUC、FDR、子集選擇與搜尋) | [KP00 特徵選擇路線圖](lectures/lec07-kp00-overview.md) · [簡報](slides/lec07-kp00-overview.jbd.json);[KP01 為什麼要選特徵](lectures/lec07-kp01-why-select.md) · [簡報](slides/lec07-kp01-why-select.jbd.json);[KP02 前置處理](lectures/lec07-kp02-preprocessing.md) · [簡報](slides/lec07-kp02-preprocessing.jbd.json);[KP03 統計檢定](lectures/lec07-kp03-hypothesis-tests.md) · [簡報](slides/lec07-kp03-hypothesis-tests.jbd.json);[KP04 ROC 曲線與 AUC](lectures/lec07-kp04-roc-auc.md) · [簡報](slides/lec07-kp04-roc-auc.jbd.json);[KP05 可分離性分數 FDR](lectures/lec07-kp05-separability-fdr.md) · [簡報](slides/lec07-kp05-separability-fdr.jbd.json);[KP06 特徵子集選擇](lectures/lec07-kp06-subset-selection.md) · [簡報](slides/lec07-kp06-subset-selection.jbd.json);[KP07 特徵搜尋](lectures/lec07-kp07-search.md) · [簡報](slides/lec07-kp07-search.jbd.json) | KP00–KP07;KP00 是本單元路線圖 |
| 8 | 10/26 | 放假(光復節補假) | | 無上課 |
| 9 | 11/02 | 期中考 Midterm Exam | | 期中考 |
| 10 | 11/09 | Feature Generation I (1) – 動機與線性表示（基底、投影、KLT／PCA、SVD） | [KP01 特徵生成動機](lectures/lec10-kp01-feature-generation-motivation.md) · [簡報](slides/lec10-kp01-feature-generation-motivation.jbd.json)；[KP02 基底、投影與重建](lectures/lec10-kp02-basis-projection.md) · [簡報](slides/lec10-kp02-basis-projection.jbd.json)；[KP03 主成分分析](lectures/lec10-kp03-pca-klt.md) · [簡報](slides/lec10-kp03-pca-klt.jbd.json)；[KP04 奇異值分解](lectures/lec10-kp04-svd.md) · [簡報](slides/lec10-kp04-svd.jbd.json) | KP01–KP04；HW01 截止 |
| 10 | 11/09 | Feature Generation I (2) – 非負與非線性表示（NMF、流形、Kernel PCA） | [KP05 非負矩陣分解](lectures/lec10-kp05-nmf.md) · [簡報](slides/lec10-kp05-nmf.jbd.json)；[KP06 非線性降維與流形](lectures/lec10-kp06-manifold.md) · [簡報](slides/lec10-kp06-manifold.jbd.json)；[KP07 核主成分分析](lectures/lec10-kp07-kernel-pca.md) · [簡報](slides/lec10-kp07-kernel-pca.jbd.json) | KP05–KP07 |
| 10 | 11/09 | Feature Generation I (3) – 圖方法（Laplacian Eigenmaps、LLE、ISOMAP） | [KP08 拉普拉斯特徵映射](lectures/lec10-kp08-laplacian-eigenmaps.md) · [簡報](slides/lec10-kp08-laplacian-eigenmaps.jbd.json)；[KP09 局部重建與圖距離](lectures/lec10-kp09-lle-isomap.md) · [簡報](slides/lec10-kp09-lle-isomap.jbd.json) | KP08–KP09 |
| 11 | 11/16 | Template Matching (1) – Matching Techniques & Distance Measures(序列樣板匹配:動機、格網路徑與代價、Bellman 動態規劃、編輯距離) | [KP01 為什麼不能直接相減](lectures/lec11-kp01-motivation.md) · [簡報](slides/lec11-kp01-motivation.jbd.json)；[KP02 格網、路徑與代價](lectures/lec11-kp02-grid-path.md) · [簡報](slides/lec11-kp02-grid-path.jbd.json)；[KP03 Bellman 最適性原理與動態規劃](lectures/lec11-kp03-dp-bellman.md) · [簡報](slides/lec11-kp03-dp-bellman.jbd.json)；[KP04 編輯距離](lectures/lec11-kp04-edit-distance.md) · [簡報](slides/lec11-kp04-edit-distance.jbd.json) | KP01–KP04;合併原計畫第 11、12 週,共 11 個知識點分三段;KP01–KP06 為必學,KP07–KP11 為自主學習 |
| 11 | 11/16 | Template Matching (2) – Dynamic Time Warping(動態時間校正:語音辨識的問題設定與特徵、端點／全域／局部限制) | [KP05 DTW：語音的問題設定與特徵](lectures/lec11-kp05-dtw-setup.md) · [簡報](slides/lec11-kp05-dtw-setup.jbd.json)；[KP06 DTW 的限制條件](lectures/lec11-kp06-dtw-constraints.md) · [簡報](slides/lec11-kp06-dtw-constraints.jbd.json) | KP05–KP06 |
| 11 | 11/16 | Template Matching (3) – Correlation, Deformable Templates & Retrieval(互相關與加速、可變形樣板、內容檢索與相關性回饋) | [KP07 互相關樣板匹配](lectures/lec11-kp07-cross-correlation.md){ .self-study } · [簡報](slides/lec11-kp07-cross-correlation.jbd.json){ .self-study }；[KP08 相關匹配的計算加速](lectures/lec11-kp08-correlation-speedup.md){ .self-study } · [簡報](slides/lec11-kp08-correlation-speedup.jbd.json){ .self-study }；[KP09 可變形樣板：內部與外部能量](lectures/lec11-kp09-deformable-energy.md){ .self-study } · [簡報](slides/lec11-kp09-deformable-energy.jbd.json){ .self-study }；[KP10 可變形樣板的三要素與公式](lectures/lec11-kp10-deformable-formulas.md){ .self-study } · [簡報](slides/lec11-kp10-deformable-formulas.jbd.json){ .self-study }；[KP11 內容檢索與相關性回饋](lectures/lec11-kp11-retrieval-feedback.md){ .self-study } · [簡報](slides/lec11-kp11-retrieval-feedback.jbd.json){ .self-study } | KP07–KP11;全部為自主學習 |
| 12 | 11/23 | Context-Dependent Classification (1) – Markov Models(情境相依分類:相鄰觀測相依、序列貝氏分類器、一階馬可夫鏈) | [KP01 相鄰觀測的相依](lectures/lec12-kp01-context.md) · [簡報](slides/lec12-kp01-context.jbd.json)；[KP02 序列的貝氏分類器](lectures/lec12-kp02-sequence-bayes.md) · [簡報](slides/lec12-kp02-sequence-bayes.jbd.json)；[KP03 一階馬可夫鏈](lectures/lec12-kp03-markov-chain.md) · [簡報](slides/lec12-kp03-markov-chain.jbd.json) | KP01–KP03;原第 13 週,提前一週;KP01–KP05 為必學,KP06–KP07 為自主學習 |
| 12 | 11/23 | Context-Dependent Classification (1) – Viterbi Algorithm(Viterbi 演算法:動態規劃、手算實例) | [KP04 Viterbi 演算法](lectures/lec12-kp04-viterbi.md) · [簡報](slides/lec12-kp04-viterbi.jbd.json)；[KP05 Viterbi 手算實例](lectures/lec12-kp05-viterbi-example.md) · [簡報](slides/lec12-kp05-viterbi-example.jbd.json) | KP04–KP05 |
| 12 | 11/23 | Context-Dependent Classification (1) – Channel Equalization(通道等化:符號間干擾、群集、狀態與有限狀態機) | [KP06 符號間干擾與群集](lectures/lec12-kp06-equalization-isi.md){ .self-study } · [簡報](slides/lec12-kp06-equalization-isi.jbd.json){ .self-study }；[KP07 狀態與有限狀態機](lectures/lec12-kp07-state-fsm.md){ .self-study } · [簡報](slides/lec12-kp07-state-fsm.jbd.json){ .self-study } | KP06–KP07;全部為自主學習 |
| 13 | 11/30 | Context-Dependent Classification (2) – Hidden Markov Models(隱藏馬可夫模型:隱藏狀態的直覺、HMM 的正式定義) | [KP01 隱藏狀態的直覺](lectures/lec13-kp01-hidden-states.md) · [簡報](slides/lec13-kp01-hidden-states.jbd.json)；[KP02 HMM 的正式定義](lectures/lec13-kp02-hmm-definition.md) · [簡報](slides/lec13-kp02-hmm-definition.jbd.json) | KP01–KP02;原第 14 週,提前一週;KP01–KP05 為必學,KP06–KP07 為自主學習 |
| 13 | 11/30 | Context-Dependent Classification (2) – HMM Recognition(辨識:任意路徑與前向—後向遞迴、最佳路徑法) | [KP03 前向後向遞迴](lectures/lec13-kp03-forward-backward.md) · [簡報](slides/lec13-kp03-forward-backward.jbd.json)；[KP04 最佳路徑辨識](lectures/lec13-kp04-best-path.md) · [簡報](slides/lec13-kp04-best-path.jbd.json) | KP03–KP04 |
| 13 | 11/30 | Context-Dependent Classification (2) – HMM Training(訓練:Baum-Welch 重估) | [KP05 Baum-Welch 重估](lectures/lec13-kp05-baum-welch.md) · [簡報](slides/lec13-kp05-baum-welch.jbd.json) | KP05 |
| 13 | 11/30 | Context-Dependent Classification (2) – HMM Training and Continuous Observations(Viterbi 重估、連續觀測與高斯混合發射) | [KP06 Viterbi 重估](lectures/lec13-kp06-viterbi-reestimation.md){ .self-study } · [簡報](slides/lec13-kp06-viterbi-reestimation.jbd.json){ .self-study }；[KP07 連續觀測與高斯混合](lectures/lec13-kp07-continuous-hmm.md){ .self-study } · [簡報](slides/lec13-kp07-continuous-hmm.jbd.json){ .self-study } | KP06–KP07;全部為自主學習 |
| 14 | 12/07 | Clustering (1) – K-means & K-medoids(硬分群:K 平均的兩步交替與局部最小、K 中心點與 PAM/CLARA/CLARANS) | [KP01 K 平均分群](lectures/lec14-kp01-kmeans.md) · [簡報](slides/lec14-kp01-kmeans.jbd.json)；[KP02 K 中心點分群](lectures/lec14-kp02-kmedoids.md) · [簡報](slides/lec14-kp02-kmedoids.jbd.json) | KP01–KP02;原第 15 週,提前一週;KP01–KP07 為必學,KP08 為自主學習 |
| 14 | 12/07 | Clustering (1) – Hierarchical Clustering(階層分群:巢狀分群、GAS 與樹狀圖、Lance–Williams 連結法) | [KP03 階層凝聚分群](lectures/lec14-kp03-hierarchical-gas.md) · [簡報](slides/lec14-kp03-hierarchical-gas.jbd.json)；[KP04 連結法與更新公式](lectures/lec14-kp04-linkage.md) · [簡報](slides/lec14-kp04-linkage.jbd.json) | KP03–KP04 |
| 14 | 12/07 | Clustering (1) – Monotonicity, Graph Methods & Cophenetic Matrix(單調性、門檻圖與最小生成樹、平手、共表型矩陣、分裂法) | [KP05 單調性與圖論方法](lectures/lec14-kp05-monotonicity-graph.md) · [簡報](slides/lec14-kp05-monotonicity-graph.jbd.json)；[KP06 共表型矩陣與分裂法](lectures/lec14-kp06-cophenetic-divisive.md) · [簡報](slides/lec14-kp06-cophenetic-divisive.jbd.json) | KP05–KP06 |
| 14 | 12/07 | Clustering (1) – Choosing the Cut Level(在哪一層切樹:叢集壽命、Method I 與 Method II) | [KP07 切樹的層級選擇](lectures/lec14-kp07-cut-level.md) · [簡報](slides/lec14-kp07-cut-level.jbd.json) | KP07 |
| 14 | 12/07 | Clustering (1) – Hierarchical Clustering for Large Data(大資料:CURE、ROCK、Chameleon) | [KP08 大資料階層分群](lectures/lec14-kp08-large-data-hierarchical.md){ .self-study } · [簡報](slides/lec14-kp08-large-data-hierarchical.jbd.json){ .self-study } | KP08;自主學習 |
| 15 | 12/14 | Clustering (2) – Evaluation & Course Project Discussion | | 原第 16 週,提前一週 |
| 16 | 12/21 | 彈性週(期末複習與專題準備) | | 因第 11、12 週合併而空出;老師 2026-11-12 決定先標為彈性週 |
| 17 | 12/28 | 期末考 / 期末專題發表 Final Exam / Project Presentation | | 期末考(學校期末評量 12/28–31) |

> 第 10 週簡報已更新為 reasoning-led-teaching-deck 2.4.1 重製審閱稿（KP01–KP09，中英文共 18 份）。KP01 已補「資料外洩」說明，KP01、KP02 已修正公式排版；最終教學稽核尚待完成。

## 英文版教材與簡報(English materials, week 7)

第 7 週 Feature Selection 的英文講義與英文原生簡報，內容與上表中文版對應；KP01 目前只有英文簡報。

- KP00 Feature selection roadmap:[Lecture](lectures/en/lec07-kp00-overview.md) · [Slides](slides/lec07-kp00-overview-en.jbd.json)
- KP01 Why select features:[Slides](slides/lec07-kp01-why-select-en.jbd.json)
- KP02 Preprocessing:[Lecture](lectures/en/lec07-kp02-preprocessing.md) · [Slides](slides/lec07-kp02-preprocessing-en.jbd.json)
- KP03 Hypothesis tests:[Lecture](lectures/en/lec07-kp03-hypothesis-tests.md) · [Slides](slides/lec07-kp03-hypothesis-tests-en.jbd.json)
- KP04 ROC curve and AUC:[Lecture](lectures/en/lec07-kp04-roc-auc.md) · [Slides](slides/lec07-kp04-roc-auc-en.jbd.json)
- KP05 Separability scores: FDR and scatter matrices:[Lecture](lectures/en/lec07-kp05-separability-fdr.md) · [Slides](slides/lec07-kp05-separability-fdr-en.jbd.json)
- KP06 Feature subset selection:[Lecture](lectures/en/lec07-kp06-subset-selection.md) · [Slides](slides/lec07-kp06-subset-selection-en.jbd.json)
- KP07 Feature search:[Lecture](lectures/en/lec07-kp07-search.md) · [Slides](slides/lec07-kp07-search-en.jbd.json)

## 英文版簡報(English slides, week 10)

第 10 週 Feature Generation I 的九個 KP 各有英文原生簡報，對應上表的繁中英講義；網站同時提供網頁版與 JBD 下載。

- KP01 Feature generation: decide what to preserve:[Slides](slides/lec10-kp01-feature-generation-motivation-en.jbd.json)
- KP02 Basis, projection and reconstruction:[Slides](slides/lec10-kp02-basis-projection-en.jbd.json)
- KP03 Principal component analysis / KLT:[Slides](slides/lec10-kp03-pca-klt-en.jbd.json)
- KP04 Singular value decomposition:[Slides](slides/lec10-kp04-svd-en.jbd.json)
- KP05 Nonnegative matrix factorization:[Slides](slides/lec10-kp05-nmf-en.jbd.json)
- KP06 Nonlinear dimensionality reduction and manifolds:[Slides](slides/lec10-kp06-manifold-en.jbd.json)
- KP07 Kernel principal component analysis:[Slides](slides/lec10-kp07-kernel-pca-en.jbd.json)
- KP08 Laplacian Eigenmaps:[Slides](slides/lec10-kp08-laplacian-eigenmaps-en.jbd.json)
- KP09 Local reconstruction and graph distances: LLE / ISOMAP:[Slides](slides/lec10-kp09-lle-isomap-en.jbd.json)

## 英文版教材(English materials, weeks 5–6)

第 5、6 週(Nonlinear Classifiers)的講義與簡報另有英文版,內容與上表中文版對應。

- Chapter 4 Route Map: After One Line Is Not Enough:[Lecture](lectures/en/lec05-kp00-overview.md) · [Slides](slides/lec05-kp00-overview-en.jbd.json)
- KP01 XOR and the limit of one line:[Lecture](lectures/en/lec05-kp01-xor.md) · [Slides](slides/lec05-kp01-xor-en.jbd.json)
- KP02 Two-Layer Perceptron: Encode Positions First, Then Classify:[Lecture](lectures/en/lec05-kp02-two-layer-perceptron.md) · [Slides](slides/lec05-kp02-two-layer-perceptron-en.jbd.json)
- KP03 Codes of several lines and the limit of two layers:[Lecture](lectures/en/lec05-kp03-polyhedral-codes.md) · [Slides](slides/lec05-kp03-polyhedral-codes-en.jbd.json)
- KP04 Three-Layer Perceptron: Detect Each Code, Then Merge:[Lecture](lectures/en/lec05-kp04-three-layer-perceptron.md) · [Slides](slides/lec05-kp04-three-layer-perceptron-en.jbd.json)
- KP05 Constructive Methods: Growing a Network from Training Points:[Lecture](lectures/en/lec05-kp05-constructive-methods.md) · [Slides](slides/lec05-kp05-constructive-methods-en.jbd.json)
- KP06 From the Step to the Gradient of Backpropagation:[Lecture](lectures/en/lec05-kp06-backprop-gradient.md) · [Slides](slides/lec05-kp06-backprop-gradient-en.jbd.json)
- KP07 The Backpropagation Algorithm:[Lecture](lectures/en/lec05-kp07-backprop-algorithm.md) · [Slides](slides/lec05-kp07-backprop-algorithm-en.jbd.json)
- KP08 Speeding Up Backpropagation (self-study):[Lecture](lectures/en/lec05-kp08-backprop-speedups.md){ .self-study } · [Slides](slides/lec05-kp08-backprop-speedups-en.jbd.json){ .self-study }
- KP09 Choosing the Cost Function:[Lecture](lectures/en/lec05-kp09-cost-functions.md) · [Slides](slides/lec05-kp09-cost-functions-en.jbd.json)
- KP10 Network size, generalization and early stopping (self-study):[Lecture](lectures/en/lec05-kp10-network-size.md){ .self-study } · [Slides](slides/lec05-kp10-network-size-en.jbd.json){ .self-study }
- KP11 Pruning, regularization and reported simulations (self-study):[Lecture](lectures/en/lec05-kp11-pruning-regularization.md){ .self-study } · [Slides](slides/lec05-kp11-pruning-regularization-en.jbd.json){ .self-study }
- KP12 Weight sharing and transformation invariance (self-study):[Lecture](lectures/en/lec05-kp12-weight-sharing.md){ .self-study } · [Slides](slides/lec05-kp12-weight-sharing-en.jbd.json){ .self-study }
- KP13 Generalized Linear Classifiers:[Lecture](lectures/en/lec05-kp13-generalized-linear.md) · [Slides](slides/lec05-kp13-generalized-linear-en.jbd.json)
- KP14 Cover's Theorem (self-study):[Lecture](lectures/en/lec05-kp14-cover-theorem.md){ .self-study } · [Slides](slides/lec05-kp14-cover-theorem-en.jbd.json){ .self-study }
- KP15 Polynomial Classifiers:[Lecture](lectures/en/lec05-kp15-polynomial.md) · [Slides](slides/lec05-kp15-polynomial-en.jbd.json)
- KP16 RBF Networks:[Lecture](lectures/en/lec05-kp16-rbf.md) · [Slides](slides/lec05-kp16-rbf-en.jbd.json)
- KP17 The Universal Approximation Theorem (self-study):[Lecture](lectures/en/lec05-kp17-universal-approx.md){ .self-study } · [Slides](slides/lec05-kp17-universal-approx-en.jbd.json){ .self-study }
- KP18 The Probabilistic Neural Network (PNN):[Lecture](lectures/en/lec05-kp18-pnn.md) · [Slides](slides/lec05-kp18-pnn-en.jbd.json)
- KP19 The Nonlinear SVM and the Mercer Kernel Trick:[Lecture](lectures/en/lec05-kp19-kernel-svm.md) · [Slides](slides/lec05-kp19-kernel-svm-en.jbd.json)
- KP20 Beyond the SVM: The General Kernel Trick and the Kernel Perceptron:[Lecture](lectures/en/lec05-kp20-beyond-svm.md) · [Slides](slides/lec05-kp20-beyond-svm-en.jbd.json)
- KP21 The Representer Theorem, Kernel Expansions and Sparsification (self-study):[Lecture](lectures/en/lec05-kp21-representer.md){ .self-study } · [Slides](slides/lec05-kp21-representer-en.jbd.json){ .self-study }
- KP22 Robust Statistical Regression and Ridge Regression (self-study):[Lecture](lectures/en/lec05-kp22-robust-ridge.md){ .self-study } · [Slides](slides/lec05-kp22-robust-ridge-en.jbd.json){ .self-study }
- KP23 Decision Trees: OBCT, Splitting Criteria and Pruning:[Lecture](lectures/en/lec05-kp23-decision-tree.md) · [Slides](slides/lec05-kp23-decision-tree-en.jbd.json)
- KP24 Combining Classifiers: Product, Sum, Majority Vote and the Bayesian View:[Lecture](lectures/en/lec05-kp24-combining.md) · [Slides](slides/lec05-kp24-combining-en.jbd.json)
- KP25 Boosting and AdaBoost: Turning Weak into Strong:[Lecture](lectures/en/lec05-kp25-adaboost.md) · [Slides](slides/lec05-kp25-adaboost-en.jbd.json)
- KP26 The Class Imbalance Problem:[Lecture](lectures/en/lec05-kp26-imbalance.md) · [Slides](slides/lec05-kp26-imbalance-en.jbd.json)

## 英文版簡報(English slides, week 3)

第 3 週(Linear Classifiers)的導學版簡報另有英文版(含英文配音),內容與上表中文版對應;目前只有簡報,尚無英文講義;英文版尚未含中文版新增的推導頁與配音更新。

- KP01 Score, Normal Vector and Distance:[Slides](slides/lec03-kp01-pilot-en.jbd.json)
- KP02 Batch Perceptron:[Slides](slides/lec03-kp02-batch-perceptron-en.jbd.json)
- KP03 Perceptron Convergence Proof (self-study):[Slides](slides/lec03-kp03-convergence-en.jbd.json){ .self-study }
- KP04 Online Perceptron:[Slides](slides/lec03-kp04-online-perceptron-en.jbd.json)
- KP05 Neuron and Pocket Algorithm:[Slides](slides/lec03-kp05-neuron-pocket-en.jbd.json)
- KP06 Kesler Construction:[Slides](slides/lec03-kp06-kesler-en.jbd.json)
- KP07 Least Squares and Orthogonal Projection:[Slides](slides/lec03-kp07-mse-projection-en.jbd.json)
- KP08 LMS Algorithm:[Slides](slides/lec03-kp08-lms-en.jbd.json)
- KP09 Least-Squares Solution:[Slides](slides/lec03-kp09-least-squares-en.jbd.json)
- KP10 Conditional Mean and Best Prediction (self-study):[Slides](slides/lec03-kp10-conditional-mean-en.jbd.json){ .self-study }
- KP11 Conditional Mean and Posterior Probability (self-study):[Slides](slides/lec03-kp11-mse-posterior-en.jbd.json){ .self-study }
- KP12 Bias and Variance (self-study):[Slides](slides/lec03-kp12-bias-variance-en.jbd.json){ .self-study }
- KP13 Logistic Regression:[Slides](slides/lec03-kp13-logistic-en.jbd.json)
- KP14 Hard-Margin Support Vector Machine:[Slides](slides/lec03-kp14-hard-margin-en.jbd.json)
- KP15 Soft-Margin Support Vector Machine:[Slides](slides/lec03-kp15-soft-margin-en.jbd.json)
- KP16 Multiclass and Error-Correcting Output Codes:[Slides](slides/lec03-kp16-multiclass-ecoc-en.jbd.json)

> 重要日期若有異動,請同步更新 [`CHANGELOG.md`](CHANGELOG.md)。


