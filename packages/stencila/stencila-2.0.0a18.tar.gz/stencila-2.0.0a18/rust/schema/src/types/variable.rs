// Generated file; do not edit. See `schema-gen` crate.

use crate::prelude::*;

use super::node::Node;
use super::string::String;

/// A variable representing a name / value pair.
#[skip_serializing_none]
#[serde_as]
#[derive(Debug, SmartDefault, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, WriteNode, ReadNode)]
#[serde(rename_all = "camelCase", crate = "common::serde")]
#[derive(derive_more::Display)]
#[display(fmt = "Variable")]
pub struct Variable {
    /// The type of this item.
    pub r#type: MustBe!("Variable"),

    /// The identifier for this item.
    #[strip(metadata)]
    #[html(attr = "id")]
    pub id: Option<String>,

    /// The namespace, usually a document path, within which the variable resides
    pub namespace: String,

    /// The name of the variable.
    pub name: String,

    /// The expected type of variable e.g. `Number`, `Timestamp`, `Datatable`
    pub kind: Option<String>,

    /// The value of the variable.
    pub value: Option<Box<Node>>,
}

impl Variable {
    pub fn new(namespace: String, name: String) -> Self {
        Self {
            namespace,
            name,
            ..Default::default()
        }
    }
}
