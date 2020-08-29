import Head from 'next/head'

import Menu from '../components/Menu';

export default function Layout(props) {
    return (
        <div>
            <Head>
                <title> {props.title} </title>
            </Head>

            <header className="text-center bg-gray-200">
                <div className="w-full flex justify-center py-8">
                    <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40"></img>
                </div>
                <p className="text-2xl font-thin pb-4">Kreimben.com, Indie developer's website</p>
            </header>

            <Menu />

            <main className="bg-gray-200">
                {props.children}
            </main>
        </div>
    )
}