#include "vabamorf.h"

Analysis::Analysis(const char* root, const char* ending, const char* clitic, const char* partofspeech, const char* form)
    : root(root), ending(ending), clitic(clitic), partofspeech(partofspeech), form(form) {
}

Analysis::Analysis(const Analysis& analysis)
    : root(analysis.root), ending(analysis.ending), clitic(analysis.clitic), partofspeech(analysis.partofspeech), form(analysis.form) {
}

Analyzer::Analyzer(std::string const lexPath) {
    morf.Start(lexPath.c_str(), MF_DFLT_MORFA);
    initMorfSettings();
}

void Analyzer::initMorfSettings() {
    MRF_FLAGS_BASE_TYPE flags=MF_DFLT_MORFA;
    flags|=MF_OLETA;
    flags|=MF_KR6NKSA;
    morf.SetFlags(flags);
    morf.SetMaxTasand();
    morf.Clr();
}

void Analyzer::process(CFSArray<CFSVar>& words) {
    for (int i=0 ; i<words.GetSize() ; ++i) {
        morf.Set1(words[i]["text"].GetWString());
        morf.Tag<int>((int)i, PRMS_TAGSINT);
    }

    LYLI Lyli;
    CFSVar Analysis;
    Analysis.Cast(CFSVar::VAR_ARRAY);
    INTPTR ipLastPos=-1;
    INTPTR ipDeleted=0;

    while (morf.Flush(Lyli)) {
        if (Lyli.lipp & PRMS_TAGSINT){
            INTPTR ipPos=-ipDeleted+Lyli.ptr.arv;
            if (ipLastPos==-1) {
                words[ipPos]["analysis"]=Analysis;
                ipLastPos=ipPos;
            } else {
                words[ipLastPos]["text"]=words[ipLastPos]["text"].GetAString()+" "+words[ipPos]["text"].GetAString();
                words.RemoveItem(ipPos);
                ipDeleted++;
            }
        } else if (Lyli.lipp & PRMS_MRF) {
            Analysis.Cleanup();
            Analysis.Cast(CFSVar::VAR_ARRAY);
            ipLastPos=-1;
            Lyli.ptr.pMrfAnal->StrctKomadLahku();
            for (INTPTR ipTul=0; ipTul<Lyli.ptr.pMrfAnal->idxLast; ipTul++){
                MRFTUL Tul=*(*Lyli.ptr.pMrfAnal)[(int)ipTul];
                CFSVar Analysis1;
                Analysis1["root"]=Tul.tyvi;
                Analysis1["ending"]=Tul.lopp;
                Analysis1["clitic"]=Tul.kigi;
                Analysis1["partofspeech"]=Tul.sl;
                CFSWString szForm=Tul.vormid; szForm.TrimRight(L", ");
                Analysis1["form"]=szForm;
                Analysis[ipTul]=Analysis1;
            }
        }
    }
}

void Analyzer::compileResults(CFSArray<CFSVar>& words, std::vector<WordAnalysis>& results) {
    for (int widx=0 ; widx < words.GetSize() ; ++widx) {
        CFSVar word = words[widx];
        CFSVar analysis = word["analysis"];
        AnalysisVector vec;
        for (int aidx=0 ; aidx < analysis.GetSize() ; ++aidx) {
            CFSVar a = analysis[aidx];
            vec.push_back(Analysis(a["root"].GetAString(),
                                   a["ending"].GetAString(),
                                   a["clitic"].GetAString(),
                                   a["partofspeech"].GetAString(),
                                   a["form"].GetAString()));
        }
        results.push_back(WordAnalysis(std::string(word["text"].GetAString()), vec));
    }
}

CFSArray<CFSVar> cfsvarFromStringVector(StringVector const& sentence) {
    CFSArray<CFSVar> data(sentence.size());
    for (size_t i=0 ; i<sentence.size() ; ++i) {
        CFSVar wordData;
        wordData.Cast(CFSVar::VAR_MAP);
        wordData["text"] = sentence[i].c_str();
        data.AddItem(wordData);
    }
    return data;
}

std::vector<WordAnalysis> Analyzer::analyze(StringVector const& sentence) {
    initMorfSettings();

    CFSArray<CFSVar> words = cfsvarFromStringVector(sentence);
    process(words);

    std::vector<WordAnalysis> results;
    results.reserve(sentence.size());
    compileResults(words, results);

    return results;
}
