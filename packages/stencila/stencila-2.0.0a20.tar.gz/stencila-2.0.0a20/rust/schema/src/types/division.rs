// Generated file; do not edit. See `schema-gen` crate.

use crate::prelude::*;

use super::block::Block;
use super::cord::Cord;
use super::execution_digest::ExecutionDigest;
use super::string::String;

/// Styled block content.
#[skip_serializing_none]
#[serde_as]
#[derive(Debug, SmartDefault, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, WriteNode, ReadNode)]
#[serde(rename_all = "camelCase", crate = "common::serde")]
#[cfg_attr(feature = "proptest", derive(Arbitrary))]
#[derive(derive_more::Display)]
#[display(fmt = "Division")]
#[html(elem = "div", custom)]
#[markdown(special)]
pub struct Division {
    /// The type of this item.
    #[cfg_attr(feature = "proptest", proptest(value = "Default::default()"))]
    pub r#type: MustBe!("Division"),

    /// The identifier for this item.
    #[strip(metadata)]
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    #[html(attr = "id")]
    pub id: Option<String>,

    /// The code of the equation in the `styleLanguage`.
    #[cfg_attr(feature = "proptest-min", proptest(value = r#"Cord::new("code")"#))]
    #[cfg_attr(feature = "proptest-low", proptest(strategy = r#"r"[a-zA-Z0-9 \t]{1,10}".prop_map(Cord::new)"#))]
    #[cfg_attr(feature = "proptest-high", proptest(strategy = r#"r"[^\p{C}]{1,100}".prop_map(Cord::new)"#))]
    #[cfg_attr(feature = "proptest-max", proptest(strategy = r#"String::arbitrary().prop_map(Cord::new)"#))]
    #[jats(attr = "style")]
    pub code: Cord,

    /// The language used for the style specification e.g. css, tw
    #[serde(alias = "style-language", alias = "style_language")]
    #[cfg_attr(feature = "proptest-min", proptest(value = r#"None"#))]
    #[cfg_attr(feature = "proptest-low", proptest(strategy = r#"option::of(r"(css)|(tw)")"#))]
    #[cfg_attr(feature = "proptest-high", proptest(strategy = r#"option::of(r"[a-zA-Z0-9]{1,10}")"#))]
    #[cfg_attr(feature = "proptest-max", proptest(strategy = r#"option::of(String::arbitrary())"#))]
    #[jats(attr = "style-detail")]
    pub style_language: Option<String>,

    /// A digest of the `code` and `styleLanguage`.
    #[serde(alias = "compile-digest", alias = "compile_digest")]
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub compile_digest: Option<ExecutionDigest>,

    /// Errors that occurred when transpiling the `code`.
    #[serde(alias = "error")]
    #[serde(default, deserialize_with = "option_one_or_many")]
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub errors: Option<Vec<String>>,

    /// A Cascading Style Sheet (CSS) transpiled from the `code` property.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub css: Option<String>,

    /// A list of class names associated with the node.
    #[serde(alias = "class")]
    #[serde(default, deserialize_with = "option_one_or_many")]
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub classes: Option<Vec<String>>,

    /// The content within the division
    #[serde(deserialize_with = "one_or_many")]
    #[cfg_attr(feature = "proptest", proptest(value = "Default::default()"))]
    pub content: Vec<Block>,
}

impl Division {
    pub fn new(code: Cord, content: Vec<Block>) -> Self {
        Self {
            code,
            content,
            ..Default::default()
        }
    }
}
