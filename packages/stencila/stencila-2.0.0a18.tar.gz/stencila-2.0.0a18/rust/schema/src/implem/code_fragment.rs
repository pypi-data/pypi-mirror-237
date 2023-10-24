use crate::{prelude::*, CodeFragment};

impl CodeFragment {
    pub fn to_markdown_special(&self, _context: &MarkdownEncodeContext) -> (String, Losses) {
        let mut md = ["`", &self.code.replace('`', r"\`"), "`"].concat();

        if let Some(lang) = &self.programming_language {
            md.push('{');
            md.push_str(&lang.replace('}', r"\}"));
            md.push('}');
        }

        let losses = if self.id.is_some() {
            Losses::one("CodeFragment.id")
        } else {
            Losses::none()
        };

        (md, losses)
    }
}
