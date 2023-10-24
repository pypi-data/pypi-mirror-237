use smol_str::SmolStr;

use node_store::{automerge::ObjId, ReadNode, ReadStore};

use crate::{prelude::*, utilities::node_type, Array, Node, NodeType, Null, Object};

impl ReadNode for Node {
    fn load_null() -> Result<Self> {
        Ok(Node::Null(Null {}))
    }

    fn load_boolean(value: &bool) -> Result<Self> {
        Ok(Node::Boolean(*value))
    }

    fn load_int(value: &i64) -> Result<Self> {
        Ok(Node::Integer(*value))
    }

    fn load_uint(value: &u64) -> Result<Self> {
        Ok(Node::UnsignedInteger(*value))
    }

    fn load_f64(value: &f64) -> Result<Self> {
        Ok(Node::Number(*value))
    }

    fn load_str(value: &SmolStr) -> Result<Self> {
        Ok(Node::String(value.to_string()))
    }

    fn load_list<S: ReadStore>(store: &S, obj_id: &ObjId) -> Result<Self> {
        Ok(Node::Array(Array::load_list(store, obj_id)?))
    }

    fn load_map<S: ReadStore>(store: &S, obj_id: &ObjId) -> Result<Self> {
        let node_type = node_type(store, obj_id)?;

        let Some(node_type) = node_type else {
            // There is no type, or it does not match any known type, so load as an `Object`
            return Ok(Node::Object(Object::load_map(store, obj_id)?));
        };

        macro_rules! load_map_variants {
            ($( $variant:ident ),*) => {
                match node_type {
                    $(
                        NodeType::$variant => Ok(Node::$variant(crate::$variant::load_map(store, obj_id)?)),
                    )*

                    // It is not expected to have a map with type: "Object", but if there is,
                    // then treat it as such
                    NodeType::Object => Ok(Node::Object(Object::load_map(store, obj_id)?)),

                    NodeType::Null |
                    NodeType::Boolean |
                    NodeType::Integer |
                    NodeType::UnsignedInteger |
                    NodeType::Number |
                    NodeType::String |
                    NodeType::Array => bail!("Node::load_map unexpectedly called for {node_type}")
                }
            };
        }

        load_map_variants!(
            ArrayValidator,
            Article,
            AudioObject,
            BooleanValidator,
            Brand,
            Button,
            Call,
            CallArgument,
            Cite,
            CiteGroup,
            Claim,
            CodeBlock,
            CodeChunk,
            CodeError,
            CodeExpression,
            CodeFragment,
            Collection,
            Comment,
            ConstantValidator,
            ContactPoint,
            Cord,
            CreativeWork,
            Datatable,
            DatatableColumn,
            Date,
            DateTime,
            DateTimeValidator,
            DateValidator,
            DefinedTerm,
            Delete,
            Directory,
            Division,
            Duration,
            DurationValidator,
            Emphasis,
            EnumValidator,
            Enumeration,
            ExecutionDependant,
            ExecutionDependency,
            ExecutionDigest,
            ExecutionTag,
            Figure,
            File,
            For,
            Form,
            Function,
            Grant,
            Heading,
            If,
            IfClause,
            ImageObject,
            Include,
            Insert,
            IntegerValidator,
            Link,
            List,
            ListItem,
            MathBlock,
            MathFragment,
            MediaObject,
            MonetaryGrant,
            Note,
            NumberValidator,
            Organization,
            Paragraph,
            Parameter,
            Periodical,
            Person,
            PostalAddress,
            Product,
            PropertyValue,
            PublicationIssue,
            PublicationVolume,
            Quote,
            QuoteBlock,
            Review,
            Section,
            SoftwareApplication,
            SoftwareSourceCode,
            Span,
            Strikeout,
            StringValidator,
            Strong,
            Subscript,
            Superscript,
            Table,
            TableCell,
            TableRow,
            Text,
            ThematicBreak,
            Thing,
            Time,
            TimeValidator,
            Timestamp,
            TimestampValidator,
            TupleValidator,
            Underline,
            Variable,
            VideoObject
        )
    }
}
