import org.ansj.domain.Result;
import org.ansj.domain.Term;
import org.ansj.splitWord.analysis.ToAnalysis;
import java.util.*;
import java.io.*;


public class AnsjStatisticFre {
    private List<File> fileList = new ArrayList<File>();
    private Set<String> expectedNature = new HashSet<String>();
    private Map<String, Integer> word_freq = new HashMap<String, Integer>();

    public int GetFileSize() {
      return this.fileList.size();
    }

    public int Init(String filePath) {
      //遍历文件夹
      File dir = new File(filePath);
      File[] files = dir.listFiles(); // 该文件目录下文件全部放入数组
      if (files == null) {
        System.out.println("maybe dir not right");
        return 0;
      }

      for (int i = 0; i < files.length; i++) {
        String fileName = files[i].getName();
        if (files[i].isDirectory()) { // 判断是文件还是文件夹
          this.Init(files[i].getAbsolutePath()); // 获取文件绝对路径
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
    public void start(String res_file) {
        for (int i = 0; i < this.fileList.size(); i++) {
          BufferedReader reader = null;
          try {
            reader = new BufferedReader(new FileReader(new File(this.fileList.get(i).getAbsolutePath())));
            String temp_str = null;
            String total_string = null;
            while ((temp_str = reader.readLine()) != null) {
              total_string += temp_str;
            }
            Result result = ToAnalysis.parse(total_string);
            List<Term> terms = result.getTerms();
            for(int j=0; j<terms.size(); j++) {
              String natureStr = terms.get(j).getNatureStr();
              if(this.expectedNature.contains(natureStr)) {
                if (this.word_freq.containsKey(terms.get(j).getName()) != false) {
                  int count = this.word_freq.get(terms.get(j).getName()) + 1;
                  this.word_freq.put(terms.get(j).getName(), count);
                }
                else {
                  this.word_freq.put(terms.get(j).getName(), 1);
                }
              }
            }
          } catch (IOException e) {
            System.out.println(e.getMessage());
            continue;
          }
        }

        try {
          System.out.println("begin write result");
          FileWriter fw = new FileWriter(res_file);
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
        } catch (IOException e) {
          System.out.println("write result err");
          System.out.println(e.getMessage());
        }
      }

    public static void main(String[] args) {
        AnsjStatisticFre fa = new AnsjStatisticFre();
        String file_path = "./";
        String conf_file = "";
        String result_file = "";
        if (fa.Init(file_path) < 1) {
          System.out.println("init error " + file_path);
        }
        else {
          System.out.printf("file list len %d\n", fa.GetFileSize());
        }
        fa.start(result_file);
    }
}
