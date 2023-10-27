// Generated file; do not edit. See `schema-gen` crate.

use crate::prelude::*;

use super::inline::Inline;
use super::string::String;

/// A suggestion to delete some inline content.
#[skip_serializing_none]
#[serde_as]
#[derive(Debug, SmartDefault, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, WriteNode, ReadNode)]
#[serde(rename_all = "camelCase", crate = "common::serde")]
#[cfg_attr(feature = "proptest", derive(Arbitrary))]
#[derive(derive_more::Display)]
#[display(fmt = "Delete")]
#[html(elem = "del", custom)]
#[jats(special)]
#[markdown(format = "<del>{content}</del>")]
pub struct Delete {
    /// The type of this item.
    #[cfg_attr(feature = "proptest", proptest(value = "Default::default()"))]
    pub r#type: MustBe!("Delete"),

    /// The identifier for this item.
    #[strip(metadata)]
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    #[html(attr = "id")]
    pub id: Option<String>,

    /// The content that is suggested to be inserted or deleted.
    #[serde(deserialize_with = "one_or_many")]
    #[cfg_attr(feature = "proptest-min", proptest(strategy = r#"vec(Just(Inline::Text(crate::Text::from("text"))), size_range(1..=1))"#))]
    #[cfg_attr(feature = "proptest-low", proptest(strategy = r#"vec_inlines_non_recursive(1)"#))]
    #[cfg_attr(feature = "proptest-high", proptest(strategy = r#"vec_inlines_non_recursive(2)"#))]
    #[cfg_attr(feature = "proptest-max", proptest(strategy = r#"vec_inlines_non_recursive(4)"#))]
    pub content: Vec<Inline>,
}

impl Delete {
    pub fn new(content: Vec<Inline>) -> Self {
        Self {
            content,
            ..Default::default()
        }
    }
}
