use rocket::serde::{Serialize, Deserialize};


#[derive(Serialize, Deserialize, Debug)]
pub struct Success {
    success: bool,
    content: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct Fail {
    success: bool,
    content: String,
}
