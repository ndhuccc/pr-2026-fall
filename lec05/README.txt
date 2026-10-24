圖型識別 第四章 KP01：XOR 與線性分類的限制 — 逐字稿審閱版

對象：大學三年級。語言：繁體中文。狀態：草稿，待教師審閱。

閱讀入口：kp01-transcript-review.pdf（GitHub可預覽，亦可下載）
網頁版：kp01-transcript-review.html（下載後以瀏覽器開啟）
逐頁純文字：script/lec05-kp01-p001.txt 至 p012.txt。
第9–12頁為延伸閱讀；來源簡報有12個內容頁，另排除1個根場景導覽停點。
lec05沿用課程第5週檔名前綴，內容仍為第四章。

本次僅保存逐字稿，未生成音檔，未接入播放器，未上線課程網站。
來源簡報草稿已另存於 materials/lec05-kp01-xor.jbd.json；manifest保留雜湊與真實stepId，12份TXT對應同一版本。

檢查：逐頁內容對照警告0，12份TXT與工作資料一致。教師尚未審閱，reviewed全部保留false。
下載：在GitHub開啟PDF後使用下載按鈕；純文字可用Raw檢視並儲存。

講義與簡報草稿（待教師驗收，未上線網站）

materials/lec05-kp01-xor-lecture.pdf：講義PDF，GitHub可預覽及下載。
materials/lec05-kp01-xor-reading.html：離線講義閱讀版。
materials/lec05-kp01-xor.html：離線簡報，12內容頁加1導覽步驟。
materials/lec05-kp01-xor.jbd.json：可編輯JianBauDau原檔。
materials/KP01-XOR-review.zip：完整下載包，含Markdown、圖檔、繪圖程式及原有目錄結構。
materials/preview-1.png、preview-2.png：近似預覽縮圖，不是JianBauDau原生畫面。

HTML請下載後以瀏覽器開啟。講義閱讀版與簡報HTML請放在同一資料夾，讓講義中的簡報連結正常運作。
正式教材尚未寫入lectures/、slides/或assets/，也未同步課程進度表；先存於此處，以免先行發布。
原生播放器與其PDF匯出仍待驗收。8頁主線工具估28分鐘，4頁延伸不計；原先暫配15分鐘的時間差異待整章配置調整。
本次沒有漫畫、音檔。逐字稿另見同目錄的審閱版與script/。

下一批KP02–KP05講義與簡報（草稿，待教師驗收）

每個KP在materials/提供同名的 -lecture.pdf、-reading.html、.html簡報、.jbd.json原檔及-review.zip完整來源包。
KP02：lec05-kp02-two-layer-perceptron（講義8頁；簡報9個內容頁）
KP03：lec05-kp03-polyhedral-codes（講義8頁；簡報10個內容頁）
KP04：lec05-kp04-three-layer-perceptron（講義8頁；簡報11個內容頁）
KP05：lec05-kp05-constructive-methods（講義12頁；簡報13個內容頁）

合計43個內容頁；每份HTML另有1個根Frame導覽步驟。
計畫與檢查說明：materials/KP02-KP05-plan.txt、KP02-KP05-report.txt。
本批沒有漫畫、逐字稿、音檔。未正式發布課程網站；下一批KP06–KP09尚未製作，其中KP08規劃為自主學習。

保留更正：兩層網路不只可形成凸區域；三層表示足夠不等於每次tiling都只長三層。
圖與算例均有來源或補充標示；純化例是解析教學構造，不宣稱pocket實驗或完整原演算法重現。
已完成公式驗算、43頁近似預覽及雙尺寸HTML檢查；原生JianBauDau播放與其PDF匯出仍待驗收。

KP03重做版（2026-10-24，草稿，待教師驗收）

依 view-from-text 新增的 C12–C18（術語先白話、標題講明白、疑問接力、空間內容必有圖）重做 KP03，取代前一版：
materials/lec05-kp03-polyhedral-codes.*：簡報（11頁：主線9頁＋延伸2頁）、離線簡報HTML、講義PDF、講義閱讀HTML、完整來源包（含繪圖程式、術語表、稽核與冷讀者紀錄）。
本版為每頁配代數與幾何對照圖（共11張，含立方體圖、缺口圖、中點圖等補充圖）；已通過 check_slides.py 與 audit_deck.py（FAIL 0）。
冷讀者檢查做兩輪（獨立子代理），評分仍為3/5，詳見來源包內 COLD_READER.md；原生JianBauDau播放與PDF匯出尚未驗收。
KP01、KP02、KP04、KP05仍為舊版，待依新規範重做。

KP03中文版與英文版（2026-10-24，分開製作，可分別下載；草稿，待教師驗收）

中文版：materials/lec05-kp03-polyhedral-codes-zh-download.zip（簡報HTML、簡報原檔、講義PDF、講義閱讀HTML、Markdown、圖檔）。
英文版：materials/lec05-kp03-polyhedral-codes-en-download.zip（內容相同，另寫英文，不是機器剪貼）。
同一批檔案也單獨放在 materials/：lec05-kp03-polyhedral-codes-zh.* 與 -en.*（.jbd.json、.html、-lecture.pdf、-reading.html）。
先前的中英對照版保留不動（lec05-kp03-polyhedral-codes.*）；教師決定採用哪一套後，再刪除不用的版本。
兩個單語簡報都通過 check_slides.py 與 audit_deck.py --monolingual（FAIL 0）；兩份講義通過 audit_lecture.py --lang（FAIL 0）。
英文版的簡報標題、術語卡、講者備註、圖的替代文字與講義全部另寫；來源包（-review.zip）含兩種語言的組裝程式與術語表。
