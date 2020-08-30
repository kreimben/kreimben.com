import Layout from '../components/Layout'

import {loremIpsum} from '../components/loremipsum'

export default function Home() {
    return (
        <>
            <Layout title="Kreimben::Home">
                <main className="flex justify-center">
                    <div className="w-4/5 py-32 my-6 shadow-xl rounded-lg bg-gray-300 flex justify-center">
                        <p className="font-semibold text-6xl">iOS, macOS, and anything!</p>
                    </div>
                </main>
                    <p>{loremIpsum}</p>
                    <p>{loremIpsum}</p>
            </Layout>
        </>
    )
}