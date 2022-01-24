use reqwest::Response;

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

        let client = reqwest::Client::new();
        let response: Response = client
            .get(complete)
            .header("Accept", "application/json")
            .send()
            .await
            .unwrap();

        println!("{:#?}", response);

        //let json: Value = serde_json::from_str(&response).expect("There is no error!");

        //println!("{:#?}", json);

        vec![Post {}]
    }

    fn get_token(&self) -> String {
        //fs::read_to_string("/instagram_token").expect("Something went wrong reading the file!")

        String::from("IGQVJXQkQ5UGIzeTN2RlQ3NHB1SjZAfZAGt4NHZATV0ZAjQVVaXzUtdnByaWFEYnRPbHJ2QjhiSWxfVXRJQ3JMU0JoLUZAWbUJEZA2JiU2djdTRyYk9XXzZATby1UemRuVnJGMFNGb2ZApaGFKUTl5WGNKZAl9UdwZDZD")
    }
}
