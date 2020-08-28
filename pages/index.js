import Layout from '../components/Layout'

export default function Home() {
    return (
        <>
            <header className="text-center">
                <div className="w-full flex justify-center py-8">
                    <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40"></img>
                </div>
                <p className="text-2xl font-thin pb-4">Kreimben.com, Indie developer's website</p>
            </header>
            <Layout title="Kreimben.com">
                <main>
                    <h1 className="">Home page</h1>
                </main>
            </Layout>
        </>
    )
}