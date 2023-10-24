use crate::{prelude::*, Cord, Text};

impl Text {
    pub fn to_jats_special(&self) -> (String, Losses) {
        use codec_jats_trait::encode::escape;

        (escape(self.value.as_str()), Losses::none())
    }
}

impl<S> From<S> for Text
where
    S: AsRef<str>,
{
    fn from(value: S) -> Self {
        Self::new(Cord::new(value))
    }
}
