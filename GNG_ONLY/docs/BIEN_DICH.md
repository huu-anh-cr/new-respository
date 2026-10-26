# Biên dịch tài liệu GNG

HE_AGENT_GNG.tex là tài liệu LaTeX độc lập. Các hình vẽ dùng TikZ, không cần file hình ngoài.

PDF đi kèm được biên dịch thật bằng Tectonic 0.17.0+20260731 (XeTeX), không phải bản PDF dựng lại từ văn bản.

Từ thư mục docs, dùng một trong các cách:

```powershell
tectonic -X compile HE_AGENT_GNG.tex
```

hoặc với TeX Live/MiKTeX có font Latin Modern và các gói trong preamble:

```powershell
xelatex -interaction=nonstopmode -halt-on-error HE_AGENT_GNG.tex
xelatex -interaction=nonstopmode -halt-on-error HE_AGENT_GNG.tex
```

Tectonic có thể tải các gói công khai còn thiếu ở lần biên dịch đầu. Không cần tài khoản model để biên dịch tài liệu.
Tài liệu CLI: https://tectonic-typesetting.github.io/book/latest/v2cli/compile.html

COMPILE_RECEIPT.json ghi phiên bản compiler và hash file cuối cùng. Các file log/cache biên dịch không nằm trong ZIP.
