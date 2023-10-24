use std::str::FromStr;

use common::{once_cell::sync::Lazy, regex::Regex};

use crate::{prelude::*, Person, PersonOptions};

impl FromStr for Person {
    type Err = ErrReport;

    fn from_str(string: &str) -> Result<Self, Self::Err> {
        use human_name::Name;

        Ok(if let Some(name) = Name::parse(string) {
            let given_names = if let Some(first_name) = name.given_name() {
                let mut given_names = vec![first_name.to_string()];
                if let Some(middle_names) = name.middle_names() {
                    let mut middle_names = middle_names
                        .iter()
                        .map(|str| str.to_string())
                        .collect::<Vec<String>>();
                    given_names.append(&mut middle_names)
                }
                Some(given_names)
            } else {
                None
            };

            let family_names = if name.surnames().is_empty() {
                None
            } else {
                Some(
                    name.surnames()
                        .iter()
                        .map(|str| str.to_string())
                        .collect::<Vec<String>>(),
                )
            };

            let honorific_prefix = name.honorific_prefix().map(String::from);

            let honorific_suffix = name.honorific_suffix().map(String::from);

            // Note: currently not using the "generational suffix" e.g "Jr" parsed
            // by `human_name`.

            static EMAIL_REGEX: Lazy<Regex> =
                Lazy::new(|| Regex::new("<([^@]+@.+)>").expect("Unable to create regex"));
            let emails = EMAIL_REGEX
                .captures(string)
                .map(|email| vec![email[1].to_string()]);

            static URL_REGEX: Lazy<Regex> =
                Lazy::new(|| Regex::new("\\((https?://[^)]+)\\)").expect("Unable to create regex"));
            let url = URL_REGEX.captures(string).map(|url| url[1].to_string());

            Self {
                given_names,
                family_names,
                options: Box::new(PersonOptions {
                    honorific_prefix,
                    honorific_suffix,
                    emails,
                    url,
                    ..Default::default()
                }),
                ..Default::default()
            }
        } else {
            Self {
                given_names: Some(vec![string.to_string()]),
                ..Default::default()
            }
        })
    }
}
