# Codex / generic-agent — data-cleaning-pandas

Pipeline order:
1. encoding_repair → utf-8
2. read with explicit dtype + parse_dates + na_values
3. profile + dq_score
4. tidy_check
5. type coercion (errors='coerce')
6. missing-value imputation (advisor-recommended)
7. duplicate dedupe (natural keys)
8. outlier panel
9. string cleanup
10. categorical recode
11. write Parquet + manifest

See `SKILL.md`.
