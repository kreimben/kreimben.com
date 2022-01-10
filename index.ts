import * as insta from "./src/insta";

function mainInit(): void {
    alert("load main page!");

    insta.getPosts();

    const app = document.getElementById("App");
    app.innerHTML="<b1>Hello world!</b1>";
}
