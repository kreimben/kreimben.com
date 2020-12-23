import fs from 'fs';

const titleConverter = (title: string) => {
    const real = title.split("/")[2];

    if (!real.includes(".png") && real !== 'data') {
        return changeSpace(real);
    } else {
        return null;
    }
}

const changeSpace = (title: string) => {

    return title.replaceAll('%20', ' ');
}

const getPost = async (title: string) => {
    const realTitle = titleConverter(title);

    if (realTitle != null) {
        try {
            console.log("File name is " + realTitle);
            const result = fs.readFileSync('./content/posts/' + realTitle + '.mdx', 'utf-8');
            return result;
        } catch (err) { 
            console.log(err); 
            throw new Error("Error to fs");
        }
    }
}

export default getPost;
export { titleConverter };