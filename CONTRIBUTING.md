# 参与贡献 / Contributing

欢迎改进餐饮准确性、理论来源、语言和安装说明。 / Improvements to restaurant accuracy, sources, language and installation are welcome.

1. **说明问题 / State the problem.** 指出文件、句子、场景和影响。 Identify the file, wording, use case and impact.
2. **理论附来源 / Source theories.** 优先原著节选、访谈、机构资料，标明引用/转述与实际核对范围。 Prefer original excerpts, interviews or institutional sources; distinguish quotations, paraphrases and review scope.
3. **餐饮有依据 / Support food claims.** 虚构示范标明虚构，真实资料脱敏并取得必要授权。 Label fictional examples; remove identifying data and secure rights for real assets.
4. **双语同步 / Maintain parity.** 行为或方法改动同步中英文。 Update both language counterparts for behavior/method changes.
5. **保持十法三选 / Keep the contract.** 固定十个方法 ID，三条推荐来自原十条。范围变化先讨论并更新版本。 Keep method IDs and select from the original ten; discuss and version scope changes.
6. **说明图片 / Document visuals.** 提供来源、制作方式、权限与替代文字，不上传未授权肖像、标志、客户照片。 Include provenance, production method, rights and alt text; no unauthorized portraits, logos or client photos.
7. **运行检查 / Validate.** 在 PR 中记录检查结果与未验证项。 Report the following checks and remaining limits.

```bash
python3 scripts/verify_release.py
python3 -B -m unittest discover -s skills/baocanmou-restaurant-slogan/tests -v
```

贡献者应有必要权利，并按项目 MIT 许可提交；无需转让版权。请勿添加追踪、凭据、自动发布、未核实的“大师公式”或虚构增长数字。

Contributors must hold necessary rights and submit under MIT; copyright assignment is not required. Do not add tracking, credentials, automatic publishing, unsupported formulas or fabricated performance numbers.
