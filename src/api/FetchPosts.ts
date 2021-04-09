const baseURL = "https://strapi.kreimben.com/";

const FetchPostsFromMainView = async (options = ""): Promise<any> => {
    let postfix = null;
    if (options !== null || options !== undefined) {
        postfix = options;
    }

    const op = {
        method: "GET"
    }

    const completeURL = baseURL + "posts" + postfix + "/";
    //alert(completeURL);
    const response = await fetch(completeURL, op);
    return response;
}

export { FetchPostsFromMainView };