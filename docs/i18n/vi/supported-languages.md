# Ngôn ngữ được hỗ trợ

Co-op Translator hỗ trợ các mã ngôn ngữ sau cho đầu ra dịch văn bản, sổ tay và hình ảnh.

Nếu bạn muốn thêm ngôn ngữ mới, cập nhật ánh xạ ngôn ngữ và phông chữ trong `src/co_op_translator/fonts/` và kiểm tra ngôn ngữ trước khi mở pull request.

| Language Code | Tên ngôn ngữ | Phông chữ | Hỗ trợ RTL | Các vấn đề đã biết |
| --- | --- | --- | --- | --- |
| en | Tiếng Anh | NotoSans-Medium.ttf | Không | Không |
| fr | Tiếng Pháp | NotoSans-Medium.ttf | Không | Không |
| es | Tiếng Tây Ban Nha | NotoSans-Medium.ttf | Không | Không |
| de | Tiếng Đức | NotoSans-Medium.ttf | Không | Không |
| ru | Tiếng Nga | NotoSans-Medium.ttf | Không | Không |
| ar | Tiếng Ả Rập | NotoSansArabic-Medium.ttf | Có | Không |
| fa | Tiếng Ba Tư (Farsi) | NotoSansArabic-Medium.ttf | Có | Không |
| ur | Tiếng Urdu | NotoSansArabic-Medium.ttf | Có | Không |
| zh-CN | Tiếng Trung (Giản Thể) | NotoSansCJK-Medium.ttc | Không | Không |
| zh-MO | Tiếng Trung (Phồn thể, Macau) | NotoSansCJK-Medium.ttc | Không | Không |
| zh-HK | Tiếng Trung (Phồn thể, Hồng Kông) | NotoSansCJK-Medium.ttc | Không | Không |
| zh-TW | Tiếng Trung (Phồn thể, Đài Loan) | NotoSansCJK-Medium.ttc | Không | Không |
| ja | Tiếng Nhật | NotoSansCJK-Medium.ttc | Không | Không |
| ko | Tiếng Hàn | NotoSansCJK-Medium.ttc | Không | Không |
| hi | Tiếng Hindi | NotoSansDevanagari-Medium.ttf | Không | Không |
| bn | Tiếng Bengali | NotoSansBengali-Medium.ttf | Không | Không |
| mr | Tiếng Marathi | NotoSansDevanagari-Medium.ttf | Không | Không |
| ne | Tiếng Nepali | NotoSansDevanagari-Medium.ttf | Không | Không |
| pa | Tiếng Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Không | Không |
| pt-PT | Tiếng Bồ Đào Nha (Portugal) | NotoSans-Medium.ttf | Không | Không |
| pt-BR | Tiếng Bồ Đào Nha (Brazil) | NotoSans-Medium.ttf | Không | Không |
| it | Tiếng Ý | NotoSans-Medium.ttf | Không | Không |
| lt | Tiếng Litva | NotoSans-Medium.ttf | Không | Không |
| pl | Tiếng Ba Lan | NotoSans-Medium.ttf | Không | Không |
| tr | Tiếng Thổ Nhĩ Kỳ | NotoSans-Medium.ttf | Không | Không |
| el | Tiếng Hy Lạp | NotoSans-Medium.ttf | Không | Không |
| th | Tiếng Thái | NotoSansThai-Medium.ttf | Không | Không |
| sv | Tiếng Thụy Điển | NotoSans-Medium.ttf | Không | Không |
| da | Tiếng Đan Mạch | NotoSans-Medium.ttf | Không | Không |
| no | Tiếng Na Uy | NotoSans-Medium.ttf | Không | Không |
| fi | Tiếng Phần Lan | NotoSans-Medium.ttf | Không | Không |
| nl | Tiếng Hà Lan | NotoSans-Medium.ttf | Không | Không |
| he | Tiếng Do Thái | NotoSansHebrew-Medium.ttf | Có | Không |
| vi | Tiếng Việt | NotoSans-Medium.ttf | Không | Không |
| id | Tiếng Indonesia | NotoSans-Medium.ttf | Không | Không |
| ms | Tiếng Mã Lai | NotoSans-Medium.ttf | Không | Không |
| tl | Tiếng Tagalog (Filipino) | NotoSans-Medium.ttf | Không | Không |
| sw | Tiếng Swahili | NotoSans-Medium.ttf | Không | Không |
| hu | Tiếng Hungary | NotoSans-Medium.ttf | Không | Không |
| cs | Tiếng Séc | NotoSans-Medium.ttf | Không | Không |
| sk | Tiếng Slovak | NotoSans-Medium.ttf | Không | Không |
| ro | Tiếng Romania | NotoSans-Medium.ttf | Không | Không |
| bg | Tiếng Bulgaria | NotoSans-Medium.ttf | Không | Không |
| sr | Tiếng Serbia (Cyrillic) | NotoSans-Medium.ttf | Không | Không |
| hr | Tiếng Croatia | NotoSans-Medium.ttf | Không | Không |
| sl | Tiếng Slovenia | NotoSans-Medium.ttf | Không | Không |
| uk | Tiếng Ukraina | NotoSans-Medium.ttf | Không | Không |
| my | Tiếng Myanmar (Miến Điện) | NotoSansMyanmar-Medium.ttf | Không | Không |
| ta | Tiếng Tamil | NotoSansTamil-Medium.ttf | Không | Không |
| et | Tiếng Estonia | NotoSans-Medium.ttf | Không | Không |
| pcm | Tiếng Pidgin Nigeria | NotoSans-Medium.ttf | Không | Không |
| te | Tiếng Telugu | NotoSans-Medium.ttf | Không | Không |
| ml | Tiếng Malayalam | NotoSans-Medium.ttf | Không | Không |
| kn | Tiếng Kannada | NotoSans-Medium.ttf | Không | Không |
| km | Tiếng Khmer | NotoSansKhmer-Medium.ttf | Không | Không |

## Thêm một ngôn ngữ

Để thêm hỗ trợ cho một ngôn ngữ mới:

1. Thêm mã ngôn ngữ và tên hiển thị vào các tiện ích ngôn ngữ.
2. Thêm hoặc ánh xạ một phông chữ trong `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Kiểm tra đầu ra dịch Markdown và hình ảnh.
4. Mở một pull request với ánh xạ và ghi chú xác nhận.