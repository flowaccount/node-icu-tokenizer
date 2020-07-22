
#include <napi.h>
#include <unicode/brkiter.h>
#include <unicode/errorcode.h>
#include <unicode/unistr.h>

Napi::Array GetWordBoundaryPositions(const Napi::CallbackInfo& info) {
    Napi::Env env = info.Env();
    Napi::HandleScope scope(env);

   
    if (info.Length() != 2) {
        throw Napi::TypeError::New(env, Napi::String::New(env, "must supply locale and text"));
        // return;
    }

    if (!info[0].IsString()) {
        throw env,Napi::TypeError::New(env, Napi::String::New(env, "text is not specified"));
        // return;
    }

    if (!info[1].IsString()) {
        throw Napi::TypeError::New(env, Napi::String::New(env, "locale is not specified"));
        // return;
    }

   
    // // convert v8 locale to ICU
    Napi::String locale(info[1].ToString());
    const char delim[4] = "_"; 
    const char* country;
    const char* localeArg = locale.ToString().Utf8Value().c_str();
    country  = strtok((char *)localeArg, delim);
    const char* language;
    language = strtok(NULL, delim);
    Locale icuLocale(language, country);


    // // create the BreakIterator instance
    UErrorCode err = U_ZERO_ERROR;
    BreakIterator *iterator = BreakIterator::createWordInstance(icuLocale, err);
    if (U_FAILURE(err)) {
        ErrorCode errCode;
        errCode.set(err);
        throw Napi::TypeError::New(env, Napi::String::New(env, errCode.errorName()));
        // return;
    }

    // // Convert v8 text to ICU Unicode value
    Napi::String textStr = info[0].ToString();
    Napi::String textValue(textStr);
    
    UnicodeString uTextValue(textValue.ToString().Utf8Value().c_str(), "UTF-8");
    if (uTextValue.isBogus()) {
        throw Napi::TypeError::New(env, Napi::String::New(env, "unable to create unicode string"));
        // return;
    }

    iterator->setText(uTextValue);

    // // populate boundaries
    Napi::Array results = Napi::Array::New(env);
    int32_t arrayPosition = 0;
    int32_t currentBoundary = iterator->first();
    int32_t previousBoundary = 0;

    while (currentBoundary != BreakIterator::DONE) {
        if (currentBoundary > 0) {
            Napi::Object boundaryResult = Napi::Object::New(env);
            boundaryResult.Set(Napi::String::New(env, "start"), Napi::Number::New(env, previousBoundary));
            boundaryResult.Set(Napi::String::New(env, "end"), Napi::Number::New(env, currentBoundary));
            results.Set(arrayPosition++, boundaryResult);
        }

        previousBoundary = currentBoundary;
        currentBoundary = iterator->next();
               
    }

    // // cleanup
    delete iterator;

    return results;
    // info.GetReturnValue().Set(results);
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set("getWordBoundaryPositions",
              Napi::Function::New(env, GetWordBoundaryPositions));
  return exports;
}

NODE_API_MODULE(node_icu_tokenizer, Init);

