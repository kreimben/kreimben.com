import Layout from '../components/Layout'

export default function Home() {
    return (
        <>
            <header className="h-40 text-center bg-blue-400">
                <p>Hello, kreimben!</p>
            </header>
            <Layout title="Kreimben.com">
                <main>
                    <h1 className="">Home page</h1>
                </main>
            </Layout>
        </>
    )
}