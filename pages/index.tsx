import Layout from '../components/Layout'

export default function Home() {
    return (
        <>
            <Layout title="Kreimben::Home" isHome={true}>
                <div className="flex justify-center text-center">
                    <div className="bg-gray-300 p-8 m-12 rounded-lg w-4/5 text-4xl font-serif">
                        Welcome to indie developer's website!
                    </div>
                </div>
                <main className="flex justify-center">
                    <div className="w-4/5 py-32 mb-12 shadow-xl rounded-lg bg-gradient-to-r from-teal-300 to-blue-500 text-center">
                        <p className="text-4xl font-serif">I code</p>
                        <p className="font-semibold text-6xl">iOS, macOS, and anything!</p>
                    </div>
                </main>
            </Layout>
        </>
    )
}