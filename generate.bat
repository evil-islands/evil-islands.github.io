for /R %%I in (*.template) do _build\html_md_mix.py "%%I" "%%~dpnI"
