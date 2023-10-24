use crate::{encode::attr, HtmlCodec};

impl HtmlCodec for bool {
    fn to_html_parts(&self) -> (&str, Vec<String>, Vec<String>) {
        (
            "span",
            vec![attr("is", "stencila-boolean")],
            vec![self.to_string()],
        )
    }

    fn to_html_attr(&self) -> String {
        self.to_string()
    }
}
