# GNG ONLY

Gói riêng gồm rules, skills, launcher và script của hệ @gng cùng phụ thuộc biên tập đã tách cục bộ. Không có token, cấu hình global hoặc bridge của hệ khác.

## Nội dung

- .agents/rules/gng_models.md và 8 skill GNG nguồn.
- gng1.py đến gng8.py: giữ nguyên launcher nguồn. Engine đích ở ngoài nguồn và chưa nằm trong gói này.
- gng7-book-editorial: script sách, renderer và audit DOCX.
- gng-smooth-book: pipeline làm mượt, Word styler và CPSI đã tách riêng.
- ext-agy-auto-resume: tiện ích quota tùy chọn của Gemini, chỉ dùng khi chủ động yêu cầu.
- docs/HE_AGENT_GNG.tex và docs/HE_AGENT_GNG.pdf: tài liệu trình bày hệ GNG.
- docs/SOURCE_INDEX.csv và SOURCE_PROVENANCE.json: căn cứ nguồn và thay đổi.
- check_gng.py, verify_package.py và MANIFEST_SHA256.json.

## Dùng trong IDE

Giải nén vào workspace mới rồi mở bằng Antigravity để nạp .agents. Kiểm tra model và công cụ thực tế của phiên. Thử prompt @gng1 hoặc @gng2 trên dữ liệu nhỏ trước khi dùng quy trình sâu.

## Chạy script sách

Tạo môi trường riêng, cài requirements.txt, xác nhận agy hoạt động. Script gng7-book-editorial dùng --batch, không có --manifest. Script làm mượt có --input, --input-dir, --out-dir, --model, --effort và --workers. Bắt đầu workers=1.

## Giới hạn CLI

Các launcher gng1.py...gng8.py còn đường dẫn F: theo bản nguồn. Chạy python check_gng.py để nhìn thấy đích thiếu. Rules/skills trong IDE và các script sách riêng là hai cách dùng cần phân biệt với launcher CLI.

## Kiểm tra gói

Chạy python verify_package.py. Script chỉ kiểm tra byte và danh mục theo manifest, không gọi model. Việc tách gói không chạy installer, không gọi agy và không kích hoạt auto-resume.
