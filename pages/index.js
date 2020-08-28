import Layout from '../components/Layout'

export default function Home() {
    return (
        <>
            <header className="h-40 text-center bg-blue-400">
                <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex items-center justify-center w-24 h-24 "></img>
                <p className="text-2xl font-thin pt-6">Kreimben.com, Indie developer's website</p>
            </header>
            <Layout title="Kreimben.com">
                <main>
                    <h1 className="">Home page</h1>
                </main>
            </Layout>
        </>
    )
}