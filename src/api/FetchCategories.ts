const baseURL = "https://strapi.kreimben.com/";

const FetchCategories = async (options = ""): Promise<any> => {
  let postfix = null;
  if (options !== null || options !== undefined) {
    postfix = "?" + options;
  }

  const op = {
    method: "GET",
  };

  const completeURL = baseURL + "categories" + postfix;
  //alert(completeURL);
  const response = await fetch(completeURL, op);
  const json = await response.json();
  return json;
};

export { FetchCategories };
