import Head from 'next/head';

import Menu from '../components/Menu';

export default function Home() {
    return (
        <>
            <Head>
                <title>Welcome to Kreimben.com!</title>
            </Head>
            <Menu />
            <main>
                <h1 className="text-red-500">Hello, World!</h1>
            </main>
        </>
    )
}