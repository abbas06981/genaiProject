// frontend/app/page.tsx
"use client";
import { useState } from 'react';

export default function HistoryBot() {
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSearch = async () => {
        setLoading(true);
        const res = await fetch('http://localhost:8000/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question }),
        });
        const data = await res.json();
        setAnswer(data.answer);
        setLoading(false);
    };

    return (
        <main className="max-w-2xl mx-auto p-8">
            <h1 className="text-3xl font-bold mb-6 text-green-700">Pakistan History AI</h1>
            <div className="flex gap-2 mb-4">
                <input
                    className="flex-1 p-2 border rounded text-black"
                    placeholder="Ask about 1947, Quaid-e-Azam, or the Constitution..."
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                />
                <button
                    onClick={handleSearch}
                    className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
                    disabled={loading}
                >
                    {loading ? 'Thinking...' : 'Ask'}
                </button>
            </div>
            {answer && (
                <div className="p-4 bg-gray-100 rounded border-l-4 border-green-600">
                    <p className="text-gray-800">{answer}</p>
                </div>
            )}
        </main>
    );
}