for /R %%I in (*.template) do html_md_mix.py "%%I" "%%~dpnI"
