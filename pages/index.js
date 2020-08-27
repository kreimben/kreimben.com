import Head from 'next/head';

import Menu from '../components/Menu';

export default function Home() {
    return (
        <>
            <Head>
                <title>Welcome to Kreimben.com!</title>
            </Head>
            <Menu />
            <main className="bg-red-300">
                <h1 className="text-blue-200">Hello, World!</h1>
            </main>
        </>
    )
}