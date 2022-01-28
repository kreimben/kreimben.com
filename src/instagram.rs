
pub struct Instagram {
    base_url: String,
}

pub struct Post {}

impl<'str> Instagram {
    pub fn new() -> Instagram {
        Instagram {
            base_url: String::from("https://graph.instagram.com/me/media"),
        }
    }

    pub async fn get_posts<'a>(&self) -> std::vec::Vec<Post> {
        let access_token = self.get_token();

        let complete = format!(
            "{}?fields={}&access_token{}",
            self.base_url.clone(),
            "id,media_type,media_url,thumbnail_url,username,timestamp",
            access_token
        );

        vec![Post {}]
    }

    fn get_token(&self) -> String {
        String::from("IGQVJXQkQ5UGIzeTN2RlQ3NHB1SjZAfZAGt4NHZATV0ZAjQVVaXzUtdnByaWFEYnRPbHJ2QjhiSWxfVXRJQ3JMU0JoLUZAWbUJEZA2JiU2djdTRyYk9XXzZATby1UemRuVnJGMFNGb2ZApaGFKUTl5WGNKZAl9UdwZDZD")
    }
}
