use roxmltree::Document;

use codec::{
    common::eyre::{bail, Result},
    schema::{self, Article},
    DecodeOptions, Losses,
};

mod back;
mod body;
mod front;
mod utilities;

use back::decode_back;
use body::decode_body;
use front::decode_front;

use self::utilities::{extend_path, record_node_lost};

/// Decode a JATS XML string to a Stencila Schema [`Node`]
///
/// This is the main entry point for decoding. It parses the XML, and then traverses the
/// XML DOM, building an [`Article`] from it (JATS is always treated as an article, not any other
/// type of `CreativeWork`).
pub(super) fn decode(
    jats: &str,
    _options: Option<DecodeOptions>,
) -> Result<(schema::Node, Losses)> {
    let mut article = Article::default();
    let mut losses = Losses::none();

    let dom = Document::parse(jats)?;
    let root = if !dom.root_element().has_tag_name("article") {
        bail!("XML document does not have an <article> root element")
    } else {
        dom.root_element()
    };

    let path = "//article";
    for child in root.children() {
        let tag = child.tag_name().name();
        let child_path = extend_path(path, tag);
        match tag {
            "front" => decode_front(&child_path, &child, &mut article, &mut losses),
            "body" => decode_body(&child_path, &child, &mut article, &mut losses),
            "back" => decode_back(&child_path, &child, &mut article, &mut losses),
            _ => record_node_lost(path, &child, &mut losses),
        }
    }

    Ok((schema::Node::Article(article), losses))
}
