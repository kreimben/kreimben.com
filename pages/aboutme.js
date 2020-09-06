import Layout from '../components/Layout'

export default function AboutMe() {
    return (
        <Layout title="Kreimben::AboutMe" isHome={false}>
            <div className="flex justify-center" key="mainContent">
                <div className="bg-gray-300 w-4/5 rounded-lg my-16 p-8 inline-block shadow-xl text-center font-mono">
                    <p className="text-3xl">Hello! I'm iOS, macOS and Web developer!</p>
                    <br />
                    <p className="font-serif text-xl">I've been programming whatever I can express my-self since I was high school student.</p>
                </div>
            </div>

            <div className="flex justify-center">

                <div className="bg-gray-300 w-4/5 rounded-lg mb-16 p-12 inline-block shadow-xl text-center text-3xl font-serif">
                    I want to post many of things about programming and anything I'm interested!
                </div>
                
            </div>

        </Layout>
    )
}