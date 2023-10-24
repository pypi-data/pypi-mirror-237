// Generated file; do not edit. See `schema-gen` crate.

use crate::prelude::*;

/// Indicates how a `List` is ordered.
#[derive(Debug, strum::Display, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, WriteNode, SmartDefault, ReadNode)]
#[serde(crate = "common::serde")]
#[cfg_attr(feature = "proptest", derive(Arbitrary))]
pub enum ListOrder {
    Ascending,

    Descending,

    #[default]
    Unordered,
}
