import Layout from '../components/Layout'

import { loremIpsum } from '../components/loremipsum'

export default function Home() {
    return (
        <>
            <Layout title="Kreimben::Home" isHome={true}>
                <main className="flex justify-center">
                    <div className="w-4/5 py-32 my-6 shadow-xl rounded-lg bg-gradient-to-r from-teal-300 to-blue-500 flex justify-center">
                        <p className="font-semibold text-6xl">iOS, macOS, and anything!</p>
                    </div>
                </main>
                <div className="flex justify-center" key="mainContent">
                    <div className="bg-gray-300 w-4/5 rounded-lg m-8 p-4 inline-block shadow-xl text-center">
                        <p className="text-3xl">Hello! I'm iOS, macOS developer!</p>
                        <br />
                        <p></p>
                    </div>
                </div>

                <p>{loremIpsum}</p>
                <p>{loremIpsum}</p>
            </Layout>
        </>
    )
}