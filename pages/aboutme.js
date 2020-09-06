import Layout from '../components/Layout'

export default function AboutMe() {
    return (
        <Layout title="Kreimben::AboutMe" isHome={false}>
            <div className="flex justify-center" key="mainContent">
                <div className="bg-gray-300 w-4/5 rounded-lg my-16 p-8 inline-block shadow-xl text-center font-mono">
                    <p className="text-3xl">Hello! I'm iOS, macOS and Web developer!</p>
                    <br />
                    <p className="font-serif text-xl">I've been programming whatever I can express my-self.</p>
                </div>
            </div>

            <div className="flex justify-center">

                <div className="bg-gray-300 w-5/6 rounded-lg my-16 p-8 inline-block shadow-xl text-center text-5xl">
                    안녕하세요!
                </div>
                
            </div>

        </Layout>
    )
}