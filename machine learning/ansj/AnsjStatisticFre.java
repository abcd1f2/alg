import org.ansj.domain.Result;
import org.ansj.domain.Term;
import org.ansj.splitWord.analysis.ToAnalysis;
import java.util.*;
import java.io.*;


public class AnsjStatisticFre {
    private List<File> fileList = new ArrayList<File>();
    private Set<String> expectedNature = new HashSet<String>();
    private Map<String, Integer> word_freq = new HashMap<String, Integer>();
    private String result_file = new String();

    public int GetFileSize() {
      return this.fileList.size();
    }

    public int Init(String filePath, String res_file) {
      //遍历文件夹
      this.result_file = res_file;
      File dir = new File(filePath);
      File[] files = dir.listFiles(); // 该文件目录下文件全部放入数组
      if (files == null) {
        System.out.println("maybe dir not right");
        return 0;
      }

      for (int i = 0; i < files.length; i++) {
        String fileName = files[i].getName();
        if (files[i].isDirectory()) { // 判断是文件还是文件夹
          this.Init(files[i].getAbsolutePath(), this.result_file); // 获取文件绝对路径
        } else { // 判断是否是文件
          if (files[i] != null) {
            fileList.add(files[i]);
          }
        }
      }

      //只关注这些词性的词
      this.expectedNature.add("n");
      this.expectedNature.add("v");
      this.expectedNature.add("vd");
      this.expectedNature.add("vn");
      this.expectedNature.add("vf");
      this.expectedNature.add("vx");
      this.expectedNature.add("vi");
      this.expectedNature.add("vl");
      this.expectedNature.add("vg");
      this.expectedNature.add("nt");
      this.expectedNature.add("nz");
      this.expectedNature.add("nw");
      this.expectedNature.add("nl");
      this.expectedNature.add("ng");
      this.expectedNature.add("userDefine");
      this.expectedNature.add("wh");

      return 1;
    }

    //分词
    public void start() {
        for (int i = 0; i < this.fileList.size(); i++) {
          BufferedReader reader = null;
          FileReader fr = null;
          try {
            fr = new FileReader(this.fileList.get(i).getAbsolutePath());
            reader = new BufferedReader(fr);

            System.out.println("start file " + this.fileList.get(i).getAbsolutePath());
            String temp_str = new String();
            while ((temp_str = reader.readLine()) != null) {
              List<Term> terms = ToAnalysis.parse(temp_str).getTerms();
              for(int j=0; j<terms.size(); j++) {
                if(this.expectedNature.contains(terms.get(j).getNatureStr())) {
                  if (this.word_freq.containsKey(terms.get(j).getName()) != false) {
                    int count = this.word_freq.get(terms.get(j).getName()) + 1;
                    this.word_freq.put(terms.get(j).getName(), count);
                  }
                  else {
                    this.word_freq.put(terms.get(j).getName(), 1);
                  }
                }
              }
            }

            if (fr != null && reader != null) {
              fr.close();
              reader.close();
            }

            System.out.println("word freq size " + this.word_freq.size());
          } catch (Exception e) {
            System.out.println("first " + e.getMessage());
            if (fr != null && reader != null) {
              try {
                fr.close();
                reader.close();
              }
              catch (Exception ioe) {
                System.out.println("second " + ioe.getMessage());
              }
            }
            continue;
          }
        }

        try {
          System.out.println("begin write result");
          FileWriter fw = new FileWriter(this.result_file);
          BufferedWriter bw = new BufferedWriter(fw);
          for (Map.Entry<String, Integer> entry : this.word_freq.entrySet()) {
            String key = entry.getKey().toString();
            int value = entry.getValue();
            bw.write(key + " " + value);
            bw.newLine();
            bw.flush();
          }
          fw.close();
          bw.close();
          System.out.println("write result end");
        } catch (Exception e) {
          System.out.println("write result err " + e.getMessage());
        }
      }

    public static void main(String[] args) {
        AnsjStatisticFre fa = new AnsjStatisticFre();
        String file_path = "./";
        String conf_file = "";
        String result_file = "result.data";
        if (fa.Init(file_path, result_file) < 1) {
          System.out.println("init error " + file_path);
        }
        else {
          System.out.println("file list len " + fa.GetFileSize());
        }
        fa.start();
    }
}
