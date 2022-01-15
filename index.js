import { gotPosts } from './insta';

function mainInit() {
    gotPosts()

    const app = document.getElementById("App")
    app.innerHTML="<b1>Successfully loaded!</b1>"
}
