use codec::{
    common::tokio,
    schema::{
        shortcuts::{p, text},
        Article,
    },
};

use super::*;

/// Test of standalone option
#[tokio::test]
async fn standalone() -> Result<()> {
    let codec = YamlCodec {};

    let doc1 = Node::Article(Article::new(vec![p([text("Hello world")])]));

    let (yaml, _) = codec
        .to_string(
            &doc1,
            Some(EncodeOptions {
                standalone: Some(true),
                ..Default::default()
            }),
        )
        .await?;
    assert_eq!(
        yaml,
        r#"$schema: https://stencila.dev/Article.schema.json
'@context': https://stencila.dev/Article.jsonld
type: Article
content:
- type: Paragraph
  content:
  - type: Text
    value: Hello world
"#
    );

    let (doc2, _) = codec.from_str(&yaml, None).await?;
    assert_eq!(doc2, doc1);

    Ok(())
}
