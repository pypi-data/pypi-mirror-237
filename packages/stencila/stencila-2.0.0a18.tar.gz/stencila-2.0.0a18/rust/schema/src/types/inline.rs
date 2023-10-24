// Generated file; do not edit. See `schema-gen` crate.

use crate::prelude::*;

use super::audio_object::AudioObject;
use super::boolean::Boolean;
use super::button::Button;
use super::cite::Cite;
use super::cite_group::CiteGroup;
use super::code_expression::CodeExpression;
use super::code_fragment::CodeFragment;
use super::date::Date;
use super::date_time::DateTime;
use super::delete::Delete;
use super::duration::Duration;
use super::emphasis::Emphasis;
use super::image_object::ImageObject;
use super::insert::Insert;
use super::integer::Integer;
use super::link::Link;
use super::math_fragment::MathFragment;
use super::media_object::MediaObject;
use super::note::Note;
use super::null::Null;
use super::number::Number;
use super::parameter::Parameter;
use super::quote::Quote;
use super::span::Span;
use super::strikeout::Strikeout;
use super::strong::Strong;
use super::subscript::Subscript;
use super::superscript::Superscript;
use super::text::Text;
use super::time::Time;
use super::timestamp::Timestamp;
use super::underline::Underline;
use super::unsigned_integer::UnsignedInteger;
use super::video_object::VideoObject;

/// Union type for valid inline content.
#[derive(Debug, strum::Display, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, WriteNode, SmartDefault)]
#[serde(untagged, crate = "common::serde")]
#[cfg_attr(feature = "proptest", derive(Arbitrary))]
pub enum Inline {
    AudioObject(AudioObject),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(skip))]
    Button(Button),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(skip))]
    Cite(Cite),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(skip))]
    CiteGroup(CiteGroup),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    CodeExpression(CodeExpression),

    CodeFragment(CodeFragment),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    Date(Date),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    DateTime(DateTime),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    Delete(Delete),

    Duration(Duration),

    Emphasis(Emphasis),

    ImageObject(ImageObject),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    Insert(Insert),

    Link(Link),

    MathFragment(MathFragment),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(skip))]
    MediaObject(MediaObject),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    Note(Note),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(skip))]
    Parameter(Parameter),

    Quote(Quote),

    Span(Span),

    Strikeout(Strikeout),

    Strong(Strong),

    Subscript(Subscript),

    Superscript(Superscript),

    #[default]
    Text(Text),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    Time(Time),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    Timestamp(Timestamp),

    Underline(Underline),

    VideoObject(VideoObject),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(value = r#"Inline::Null(Null)"#))]
    Null(Null),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(strategy = r#"Boolean::arbitrary().prop_map(Inline::Boolean)"#))]
    Boolean(Boolean),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(strategy = r#"Integer::arbitrary().prop_map(Inline::Integer)"#))]
    Integer(Integer),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(skip))]
    UnsignedInteger(UnsignedInteger),

    #[cfg_attr(feature = "proptest-min", proptest(skip))]
    #[cfg_attr(feature = "proptest-low", proptest(skip))]
    #[cfg_attr(feature = "proptest-high", proptest(skip))]
    #[cfg_attr(feature = "proptest-max", proptest(value = r#"Inline::Number(1.23)"#))]
    Number(Number),
}
